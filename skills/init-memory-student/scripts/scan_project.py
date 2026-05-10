#!/usr/bin/env python3

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Optional, Tuple


DOC_EXTS = {".docx", ".doc"}
SHEET_EXTS = {".xlsx", ".xls", ".csv"}
DECK_EXTS = {".pptx", ".ppt", ".key"}
PDF_EXTS = {".pdf"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
MEMORY_DIR_NAME = "AI_专属"

BUSINESS_KEYWORDS = [
    "竞品",
    "调研",
    "培训",
    "预算",
    "复盘",
    "分析",
    "活动",
    "课程",
    "客户",
    "对标",
    "行业",
    "纪要",
    "经营",
    "运营",
    "市场",
    "营销",
    "方案",
    "计划",
    "汇报",
    "总结",
    "模板",
    "报告",
    "数据",
    "项目",
    "清单",
]

GENERIC_TERMS = {
    "项目",
    "工作",
    "资料",
    "文件",
    "文档",
    "材料",
    "报告",
    "数据",
    "方案",
    "汇报",
    "总结",
    "模板",
    "清单",
    "计划",
    "记录",
    "整理",
    "版本",
    "信息",
    "内容",
    "附件",
}

SPECIFIC_TERMS = {
    "竞品",
    "调研",
    "培训",
    "预算",
    "复盘",
    "分析",
    "活动",
    "课程",
    "客户",
    "对标",
    "行业",
    "纪要",
    "经营",
    "运营",
    "市场",
    "营销",
}

PEEK_TITLE_WEIGHTS = {
    "方案": 8,
    "计划": 8,
    "汇报": 7,
    "总结": 7,
    "模板": 7,
    "报告": 6,
}

TYPE_WEIGHTS = {
    ".docx": 40,
    ".pptx": 30,
    ".pdf": 20,
    ".xlsx": 10,
    ".doc": 8,
    ".ppt": 7,
    ".key": 6,
    ".xls": 5,
    ".csv": 4,
}

PLACEHOLDER_MARKERS = {
    "待填写",
    "待补充",
    "待更新",
    "临时草稿",
    "示例",
    "模板",
    "项目目标",
    "当前阶段",
    "下一步",
}

CHINESE_RE = re.compile(r"[\u4e00-\u9fff]+")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def file_bucket(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in DOC_EXTS:
        return "文档"
    if suffix in SHEET_EXTS:
        return "表格"
    if suffix in DECK_EXTS:
        return "演示"
    if suffix in PDF_EXTS:
        return "PDF"
    if suffix in IMAGE_EXTS:
        return "图片"
    return "其他文件"


def normalize_name(name: str) -> str:
    stem = Path(name).stem
    stem = re.sub(r"[_\-.]+", " ", stem)
    return re.sub(r"\s+", " ", stem).strip()


def chunk_leftovers(chunk: str) -> list[str]:
    if chunk in GENERIC_TERMS or len(chunk) < 2:
        return []
    if len(chunk) in {4, 6}:
        return [chunk[index:index + 2] for index in range(0, len(chunk), 2) if chunk[index:index + 2] not in GENERIC_TERMS]
    return [chunk]


def extract_tokens(text: str) -> Counter:
    counter: Counter[str] = Counter()
    cleaned = normalize_name(text)
    for fragment in CHINESE_RE.findall(cleaned):
        remainder = fragment
        matched_specific = False
        for keyword in BUSINESS_KEYWORDS:
            if keyword in fragment:
                counter[keyword] += fragment.count(keyword)
                remainder = remainder.replace(keyword, " ")
                if keyword not in GENERIC_TERMS:
                    matched_specific = True
        if matched_specific:
            for leftover in re.split(r"\s+", remainder):
                for token in chunk_leftovers(leftover):
                    if token and token not in GENERIC_TERMS:
                        counter[token] += 1
    return counter


def is_generic_name(name: str) -> bool:
    normalized = normalize_name(name)
    chinese_parts = CHINESE_RE.findall(normalized)
    if not chinese_parts:
        return True
    joined = "".join(chinese_parts)
    if joined in GENERIC_TERMS:
        return True
    return all(part in GENERIC_TERMS for part in chinese_parts)


def name_keyword_hits(name: str) -> set[str]:
    return {token for token in extract_tokens(name) if token in BUSINESS_KEYWORDS}


def name_specific_hits(name: str) -> set[str]:
    return {token for token in extract_tokens(name) if token in SPECIFIC_TERMS or token not in GENERIC_TERMS}


def has_long_descriptive_phrase(name: str) -> bool:
    normalized = normalize_name(name)
    for fragment in CHINESE_RE.findall(normalized):
        hits = name_keyword_hits(fragment)
        if len(fragment) >= 6 and len(hits) >= 2:
            return True
    return False


def build_keyword_list(folder_name: str, sub_folders: list[str], files: list[Path]) -> list[str]:
    counter: Counter[str] = Counter()
    for source in [folder_name, *sub_folders, *[path.name for path in files]]:
        counter.update(extract_tokens(source))
    ranked = sorted(counter.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
    return [token for token, _ in ranked if token and token not in GENERIC_TERMS][:10]


def pick_peek_candidates(files: list[Path]) -> list[str]:
    ranked: list[tuple[int, str]] = []
    for path in files:
        suffix = path.suffix.lower()
        if suffix not in TYPE_WEIGHTS:
            continue
        score = TYPE_WEIGHTS[suffix]
        stem = normalize_name(path.name)
        for keyword, weight in PEEK_TITLE_WEIGHTS.items():
            if keyword in stem:
                score += weight
        size = path.stat().st_size
        if 50 * 1024 <= size <= 5 * 1024 * 1024:
            score += 12
        ranked.append((score, path.name))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [name for _, name in ranked[:2]]


def clean_markdown_text(text: str) -> str:
    normalized = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    normalized = re.sub(r"^\s*[-*]\s*", "", normalized, flags=re.MULTILINE)
    normalized = re.sub(r"\s+", "", normalized)
    for marker in PLACEHOLDER_MARKERS:
        normalized = normalized.replace(marker, "")
    return normalized


def has_substantive_content(text: str) -> bool:
    cleaned = clean_markdown_text(text)
    return len(cleaned) >= 20


def section_items(text: str, headings: list[str]) -> list[str]:
    items: list[str] = []
    lines = text.splitlines()
    capture = False
    for line in lines:
        stripped = line.strip()
        if any(stripped == f"## {heading}" for heading in headings):
            capture = True
            continue
        if capture and stripped.startswith("## "):
            break
        if capture and stripped:
            stripped = re.sub(r"^[-*]\s*", "", stripped)
            stripped = re.sub(r"^\d+\.\s*", "", stripped)
            if stripped:
                items.append(stripped)
    return items[:3]


def latest_record(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    lines = read_text(path).splitlines()
    for raw in reversed(lines):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        stripped = re.sub(r"^[-*]\s*", "", stripped)
        stripped = re.sub(r"^\d+\.\s*", "", stripped)
        if stripped:
            return stripped
    return None


def load_existing_memory(root: Path) -> Tuple[Optional[str], Optional[dict]]:
    memory_dir = root / MEMORY_DIR_NAME
    if not memory_dir.exists():
        return None, None

    task_plan = memory_dir / "task_plan.md"
    if not task_plan.exists():
        return str(memory_dir), None

    task_text = read_text(task_plan)
    if not has_substantive_content(task_text):
        return str(memory_dir), None

    findings = latest_record(memory_dir / "findings.md")
    decisions = latest_record(memory_dir / "decisions.md")
    existing_memory = {
        "goal": section_items(task_text, ["项目目标"]),
        "stage": section_items(task_text, ["当前阶段", "当前进度"]),
        "next_step": section_items(task_text, ["下一步"]),
        "recent_record": findings or decisions,
    }
    return str(memory_dir), existing_memory


def detect_confidence(folder_name: str, sub_folders: list[str], files: list[Path]) -> str:
    if not files and not sub_folders:
        return "low"

    folder_generic = is_generic_name(folder_name)
    folder_specific = name_specific_hits(folder_name)
    all_specific = set()
    for item in [*sub_folders, *[path.name for path in files]]:
        all_specific.update(name_specific_hits(item))

    if not folder_generic and folder_specific and len("".join(CHINESE_RE.findall(folder_name))) >= 4:
        return "high"
    if len({token for token in all_specific if token not in GENERIC_TERMS}) >= 2:
        return "high"
    if any(has_long_descriptive_phrase(item) for item in [folder_name, *sub_folders, *[path.name for path in files]]):
        return "high"
    return "low"


def build_report(root: Path) -> dict:
    folder_name = root.name
    entries = sorted(root.iterdir(), key=lambda path: path.name)

    sub_folders = [
        path.name
        for path in entries
        if path.is_dir() and path.name != MEMORY_DIR_NAME
    ]
    files = [path for path in entries if path.is_file()]

    categorized = {
        "文档": [],
        "表格": [],
        "演示": [],
        "PDF": [],
        "图片": [],
        "其他文件": [],
    }
    for path in files:
        categorized[file_bucket(path)].append(path.name)

    memory_dir, existing_memory = load_existing_memory(root)
    status = "existing" if existing_memory else "fresh"
    confidence = detect_confidence(folder_name, sub_folders, files)

    return {
        "root": str(root.resolve()),
        "folder_name": folder_name,
        "status": status,
        "confidence": confidence,
        "memory_dir": memory_dir,
        "sub_folders": sub_folders,
        "files": categorized,
        "file_keywords": build_keyword_list(folder_name, sub_folders, files),
        "peek_candidates": pick_peek_candidates(files),
        "existing_memory": existing_memory,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan an existing project folder for init-memory-student.")
    parser.add_argument("directory", help="Project directory to scan")
    args = parser.parse_args()

    root = Path(args.directory).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Directory does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Path is not a directory: {root}")

    report = build_report(root)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
