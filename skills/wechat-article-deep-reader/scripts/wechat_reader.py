#!/usr/bin/env python3
"""微信公众号抓取并生成三级阅读笔记。"""

from __future__ import annotations

import argparse
import asyncio
import html as html_lib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright

MOBILE_WECHAT_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
    "MicroMessenger/8.0.47 NetType/WIFI Language/zh_CN"
)

PLACEHOLDER_ARTICLE = {
    "title": "未知标题",
    "account_name": "未知账号",
    "publish_time": "未知时间",
    "content_text": "正文抓取失败",
    "source_url": "",
}

PLACEHOLDER_NOTE = {
    "level1_main_thesis": "当前正文尚未完整抓取，暂无法稳定提炼文章主旨。",
    "level2_argument_chain": "当前无法识别完整论证链条，请先确认链接可访问。",
    "level3_key_details": "当前缺少可引用细节，请重试抓取后再生成。",
}


def sanitize_text(value: str) -> str:
    value = value.replace("\r", "\n")
    value = re.sub(r"[\t\u00a0]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def ensure_nwr_flag(url: str) -> str:
    parsed = urlparse(url)
    query_items = parse_qsl(parsed.query, keep_blank_values=True)
    if not any(key == "nwr_flag" for key, _ in query_items):
        query_items.append(("nwr_flag", "1"))
    normalized_query = urlencode(query_items)
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, normalized_query, parsed.fragment)
    )


def extract_with_patterns(text: str, patterns: List[str]) -> str:
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
        if match:
            return html_lib.unescape(match.group(1)).strip()
    return ""


def format_timestamp(raw_timestamp: str) -> str:
    if not raw_timestamp:
        return ""
    raw_timestamp = raw_timestamp.strip()
    if not raw_timestamp.isdigit():
        return ""
    if len(raw_timestamp) > 10:
        raw_timestamp = raw_timestamp[:10]
    try:
        dt = datetime.fromtimestamp(int(raw_timestamp))
    except Exception:
        return ""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def normalize_lines(lines: List[str]) -> List[str]:
    cleaned: List[str] = []
    seen = set()
    for line in lines:
        line = sanitize_text(line)
        if len(line) < 4:
            continue
        if line in seen:
            continue
        seen.add(line)
        cleaned.append(line)
    return cleaned


def extract_content_text(soup: BeautifulSoup) -> str:
    content_node = soup.select_one("#js_content")
    if not content_node:
        return ""
    for tag in content_node.select("script, style"):
        tag.decompose()
    raw_text = content_node.get_text("\n", strip=True)
    lines = normalize_lines(raw_text.split("\n"))
    return "\n".join(lines)


def parse_wechat_html(html_text: str, source_url: str) -> Dict[str, str]:
    soup = BeautifulSoup(html_text, "html.parser")

    title = ""
    title_node = soup.select_one("#activity-name")
    if title_node:
        title = sanitize_text(title_node.get_text(" ", strip=True))
    if not title:
        title = extract_with_patterns(
            html_text,
            [r"msg_title\s*=\s*['\"](.+?)['\"]", r"var\s+msg_title\s*=\s*['\"](.+?)['\"]"],
        )

    account_name = ""
    account_node = soup.select_one("#js_name") or soup.select_one("#js_author_name")
    if account_node:
        account_name = sanitize_text(account_node.get_text(" ", strip=True))
    if not account_name:
        account_name = extract_with_patterns(
            html_text,
            [
                r"nickname\s*=\s*htmlDecode\(['\"](.+?)['\"]\)",
                r"nickname\s*=\s*['\"](.+?)['\"]",
            ],
        )

    publish_time = ""
    publish_time_node = soup.select_one("#publish_time")
    if publish_time_node:
        publish_time = sanitize_text(publish_time_node.get_text(" ", strip=True))
    if not publish_time:
        publish_time = extract_with_patterns(
            html_text,
            [r"publish_time\s*=\s*['\"](.+?)['\"]", r"var\s+ct\s*=\s*['\"]?(\d{10,13})['\"]?"],
        )
        if publish_time.isdigit():
            publish_time = format_timestamp(publish_time)
    if not publish_time:
        create_time = extract_with_patterns(html_text, [r"create_time\s*=\s*['\"]?(\d{10,13})['\"]?"])
        publish_time = format_timestamp(create_time)

    content_text = extract_content_text(soup)

    return normalize_article(
        {
            "title": title,
            "account_name": account_name,
            "publish_time": publish_time,
            "content_text": content_text,
            "source_url": source_url,
        },
        source_url,
    )


def normalize_article(article: Dict[str, str], source_url: str) -> Dict[str, str]:
    normalized = dict(PLACEHOLDER_ARTICLE)
    normalized["source_url"] = source_url
    for key in ["title", "account_name", "publish_time", "content_text", "source_url"]:
        value = article.get(key, "") if article else ""
        if isinstance(value, str):
            value = sanitize_text(value)
        else:
            value = str(value).strip()
        if value:
            normalized[key] = value
    if len(normalized["content_text"]) < 8:
        normalized["content_text"] = PLACEHOLDER_ARTICLE["content_text"]
    return normalized


def fetch_direct(url: str) -> Tuple[bool, Dict[str, str], str]:
    target = ensure_nwr_flag(url)
    headers = {
        "User-Agent": MOBILE_WECHAT_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Referer": "https://mp.weixin.qq.com/",
    }
    request = Request(target, headers=headers, method="GET")

    try:
        with urlopen(request, timeout=25) as response:
            raw_bytes = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            html_text = raw_bytes.decode(charset, errors="ignore")
    except HTTPError as exc:
        return False, normalize_article({}, url), f"direct HTTPError: {exc.code}"
    except URLError as exc:
        return False, normalize_article({}, url), f"direct URLError: {exc.reason}"
    except Exception as exc:  # noqa: BLE001
        return False, normalize_article({}, url), f"direct Exception: {exc}"

    article = parse_wechat_html(html_text, url)
    if article["content_text"] == PLACEHOLDER_ARTICLE["content_text"]:
        return False, article, "direct parse succeeded but content missing"
    return True, article, ""


def locate_wrapper_script() -> Path | None:
    candidates = []

    if "WECHAT_READER_WRAPPER" in os.environ:
        wrapper_from_env = Path(os.environ["WECHAT_READER_WRAPPER"])
        candidates.append(wrapper_from_env)

    skill_root = Path(__file__).resolve().parents[2]
    candidates.append(skill_root / "anything-to-notebooklm/scripts/weixin_wrapper.py")
    candidates.append(Path.home() / ".codex/skills/anything-to-notebooklm/scripts/weixin_wrapper.py")
    candidates.append(Path.home() / ".claude/skills/anything-to-notebooklm/scripts/weixin_wrapper.py")
    candidates.append(
        Path.home() / ".gemini/antigravity/skills/anything-to-notebooklm/scripts/weixin_wrapper.py"
    )

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def parse_json_from_stdout(stdout: str) -> Dict:
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    for line in reversed(lines):
        try:
            payload = json.loads(line)
            if isinstance(payload, dict):
                return payload
        except json.JSONDecodeError:
            continue
    return {}


def fetch_fallback(url: str) -> Tuple[bool, Dict[str, str], str]:
    wrapper_success, wrapper_article, wrapper_error = fetch_fallback_with_wrapper(url)
    if wrapper_success:
        return True, wrapper_article, ""

    playwright_success, playwright_article, playwright_error = fetch_fallback_with_playwright(url)
    if playwright_success:
        return True, playwright_article, ""

    merged_error = " | ".join(part for part in [wrapper_error, playwright_error] if part)
    return False, playwright_article, merged_error or "fallback failed"


def fetch_fallback_with_wrapper(url: str) -> Tuple[bool, Dict[str, str], str]:
    wrapper_path = locate_wrapper_script()
    if not wrapper_path:
        return False, normalize_article({}, url), "fallback wrapper not found"

    try:
        process = subprocess.run(
            [sys.executable, str(wrapper_path), url],
            capture_output=True,
            text=True,
            timeout=90,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, normalize_article({}, url), f"fallback run error: {exc}"

    payload = parse_json_from_stdout(process.stdout)
    if not payload:
        stderr = sanitize_text(process.stderr)
        return False, normalize_article({}, url), f"fallback parse error: {stderr or 'empty stdout'}"

    article = normalize_article(
        {
            "title": payload.get("title", ""),
            "account_name": payload.get("author", "") or payload.get("account_name", ""),
            "publish_time": payload.get("publish_time", ""),
            "content_text": payload.get("content", "") or payload.get("content_text", ""),
            "source_url": payload.get("url", "") or url,
        },
        url,
    )

    if payload.get("success") and article["content_text"] != PLACEHOLDER_ARTICLE["content_text"]:
        return True, article, ""

    fallback_error = payload.get("error", "fallback returned unsuccessful payload")
    return False, article, str(fallback_error)


async def fetch_with_playwright_async(url: str) -> Tuple[bool, Dict[str, str], str]:
    target_url = ensure_nwr_flag(url)
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                headless=True, args=["--disable-blink-features=AutomationControlled"]
            )
            context = await browser.new_context(
                viewport={"width": 430, "height": 932},
                user_agent=MOBILE_WECHAT_UA,
                locale="zh-CN",
            )
            page = await context.new_page()
            try:
                await page.goto(target_url, wait_until="networkidle", timeout=50000)
                await page.wait_for_selector("#js_content", timeout=15000)
                html_text = await page.content()
            finally:
                await page.close()
                await context.close()
                await browser.close()
    except PlaywrightTimeoutError:
        return False, normalize_article({}, url), "fallback playwright timeout"
    except Exception as exc:  # noqa: BLE001
        return False, normalize_article({}, url), f"fallback playwright error: {exc}"

    article = parse_wechat_html(html_text, url)
    if article["content_text"] == PLACEHOLDER_ARTICLE["content_text"]:
        return False, article, "fallback playwright parse succeeded but content missing"
    return True, article, ""


def fetch_fallback_with_playwright(url: str) -> Tuple[bool, Dict[str, str], str]:
    try:
        return asyncio.run(fetch_with_playwright_async(url))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(fetch_with_playwright_async(url))
        finally:
            loop.close()


def split_paragraphs(content_text: str) -> List[str]:
    raw_parts = [sanitize_text(part) for part in content_text.split("\n")]
    return normalize_lines(raw_parts)


def excerpt(text: str, max_len: int = 72) -> str:
    text = sanitize_text(text)
    if len(text) <= max_len:
        return text
    return f"{text[: max_len - 1]}…"


def build_three_level_note(article: Dict[str, str]) -> Dict[str, str]:
    content_text = article.get("content_text", "")
    paragraphs = split_paragraphs(content_text)

    if not paragraphs or content_text == PLACEHOLDER_ARTICLE["content_text"]:
        return dict(PLACEHOLDER_NOTE)

    title = article.get("title", "未知标题")

    level1_focus = excerpt(paragraphs[0], 84)
    level1_main_thesis = (
        f"文章《{title}》的核心主旨集中在“{level1_focus}”。"
        "全文结构以问题引入、核心论证推进、结论收束展开。"
    )

    chain_parts: List[str] = []
    if len(paragraphs) >= 1:
        chain_parts.append(f"起点论述聚焦在“{excerpt(paragraphs[0], 70)}”。")
    if len(paragraphs) >= 2:
        chain_parts.append(f"中段进一步展开“{excerpt(paragraphs[1], 70)}”，补强主张。")
    if len(paragraphs) >= 3:
        chain_parts.append(f"后续论证通过“{excerpt(paragraphs[2], 70)}”完成逻辑递进。")
    if len(paragraphs) >= 4:
        chain_parts.append(f"收束部分落在“{excerpt(paragraphs[3], 70)}”，形成完整闭环。")
    if not chain_parts:
        chain_parts.append("正文有效段落不足，暂无法完整还原论证链条。")
    level2_argument_chain = "\n".join(chain_parts)

    detail_lines: List[str] = []
    for index, line in enumerate(paragraphs[:6], start=1):
        detail_lines.append(f"细节{index}：{excerpt(line, 90)}")
    if not detail_lines:
        detail_lines.append("暂未抽取到稳定细节。")
    level3_key_details = "\n".join(detail_lines)

    return {
        "level1_main_thesis": level1_main_thesis,
        "level2_argument_chain": level2_argument_chain,
        "level3_key_details": level3_key_details,
    }


def render_markdown(note: Dict[str, str]) -> str:
    return (
        "# 一级 主旨与框架\n"
        f"{note['level1_main_thesis']}\n\n"
        "# 二级 论证链条\n"
        f"{note['level2_argument_chain']}\n\n"
        "# 三级 关键细节与原文表达\n"
        f"{note['level3_key_details']}\n"
    )


def write_if_needed(path_str: str | None, content: str) -> None:
    if not path_str:
        return
    path = Path(path_str).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="抓取微信公众号文章并生成三级阅读笔记")
    parser.add_argument("--url", required=True, help="微信公众号文章 URL")
    parser.add_argument("--note-output", help="三级阅读笔记 Markdown 输出路径")
    parser.add_argument("--json", dest="json_output", help="JSON 输出路径")
    parser.add_argument("--force-fallback", action="store_true", help="强制使用回退抓取引擎")
    args = parser.parse_args()

    success = False
    engine_used = "none"
    article = normalize_article({}, args.url)
    errors: List[str] = []

    if not args.force_fallback:
        direct_success, direct_article, direct_error = fetch_direct(args.url)
        if direct_success:
            success = True
            engine_used = "direct"
            article = direct_article
        else:
            article = direct_article
            if direct_error:
                errors.append(direct_error)

    if not success:
        fallback_success, fallback_article, fallback_error = fetch_fallback(args.url)
        if fallback_success:
            success = True
            engine_used = "fallback"
            article = fallback_article
        else:
            if fallback_error:
                errors.append(fallback_error)
            if article["content_text"] == PLACEHOLDER_ARTICLE["content_text"]:
                article = fallback_article

    note = build_three_level_note(article)
    markdown_text = render_markdown(note)

    payload = {
        "success": success,
        "engine_used": engine_used,
        "article": article,
        "three_level_note": note,
    }

    write_if_needed(args.note_output, markdown_text)
    if args.json_output:
        write_if_needed(args.json_output, json.dumps(payload, ensure_ascii=False, indent=2))

    print(markdown_text)

    if not success and errors:
        print("抓取失败详情：" + " | ".join(errors), file=sys.stderr)

    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
