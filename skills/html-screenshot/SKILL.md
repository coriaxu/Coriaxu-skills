---
name: html-screenshot
description: 将本地 HTML 文件截图为竖版 PNG 图片。支持单文件和批量截图。当用户说"截图""网页截图""HTML 转图片""截成图片"时触发。
---

# HTML 竖版截图技能

将本地 HTML 文件通过 Chrome 无头模式截图为高清竖版 PNG。

## 触发词

"截图"、"网页截图"、"HTML 转图片"、"截成图片"、"screenshot"

## 核心命令

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --screenshot="<输出路径>.png" \
  --window-size=<宽>,<高> \
  --force-device-scale-factor=2 \
  "file:///<HTML文件的URL编码路径>" 2>/dev/null
```

## 参数说明

| 参数 | 默认值 | 说明 |
|:---|:---|:---|
| 宽度 | 800 | 视口宽度（像素），最终图片宽度为此值 x 缩放倍率 |
| 高度 | 1400 | 视口高度（像素），竖版长图建议 1200-1600 |
| 缩放倍率 | 2 | `--force-device-scale-factor`，2 为视网膜清晰度 |

## 执行规则

**文件路径处理**：
- 输入路径是本地文件系统路径，需转换为 `file:///` 协议的 URL
- 路径中的中文和特殊字符必须做 URL 编码（`%E4%B8%AD` 等）
- 可用 Python 快速编码：`python3 -c "from urllib.parse import quote; print('file:///' + quote('<绝对路径>', safe='/:'))"`

**输出路径**：
- 默认输出到与 HTML 文件同目录，文件名前缀改为 `截图-`
- 如 `邀请函-路璐.html` → `截图-路璐.png`
- 用户指定输出路径时，按用户要求

**批量截图**：
- 多个 HTML 文件时，并行执行多条 Chrome headless 命令（每条独立进程）
- 每条命令用 `&` 后台运行，最后 `wait` 等待全部完成
- 批量模式示例：

```bash
for f in /path/to/*.html; do
  name=$(basename "$f" .html)
  url=$(python3 -c "from urllib.parse import quote; print('file:///' + quote('$f', safe='/:'))")
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless=new \
    --screenshot="/path/to/截图-${name#邀请函-}.png" \
    --window-size=800,1400 \
    --force-device-scale-factor=2 \
    "$url" 2>/dev/null &
done
wait
echo "全部截图完成"
```

**尺寸调整**：
- 用户说"手机尺寸"：`--window-size=390,844`
- 用户说"iPad 尺寸"：`--window-size=810,1080`
- 用户说"宽屏/横版"：`--window-size=1440,900`
- 用户说"长图"：高度加大到 2000-3000，按内容量判断
- 默认竖版：`--window-size=800,1400`

**质量控制**：
- 截图后用 `ls -lh` 确认文件生成且大小合理（通常 1-5MB）
- 如果用户要求预览，用 Read 工具读取 PNG 文件展示

## 前置条件

- macOS 系统
- 已安装 Google Chrome（路径：`/Applications/Google Chrome.app`）
- 无需启动 Chrome GUI，headless 模式完全后台运行

## 常见问题

- **字体没渲染**：Google Fonts 等在线字体需要网络连接，确保 VPN/网络正常
- **页面截不全**：增大 `--window-size` 的高度值
- **背景变白**：HTML 的 body 必须有明确的 background-color 设置
