# fansone-downloader

CLI tool for downloading streaming videos from [fansone.co](https://fansone.co).

> **Note:** For personal use only. You must be logged in to fansone.co and have a valid subscription/purchase for the content you download.

---

## Requirements

- Python 3.11+
- ffmpeg (must be in PATH — required for HLS merging)
- A fansone.co account with access to the content

## Installation

```bash
# 1. Clone
git clone https://github.com/charles-jdong/fansone-downloader.git
cd fansone-downloader

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and fill in .env (optional, for credential-based login)
cp .env.example .env
```

## Usage

### Option A — Browser Cookies (Recommended)

Log in to fansone.co in Firefox or Chrome, then:

```bash
python main.py https://fansone.co/post/<post-id> --browser firefox
```

This uses `browser-cookie3` to grab your existing session — no password needed.

### Option B — Credentials in .env

```bash
# Edit .env with your email/password
python main.py https://fansone.co/post/<post-id>
```

### Options

```
python main.py <url> [--browser firefox|chrome] [--quality best|worst|720] [--output ./downloads] [--clear-cache]
```

| Flag | Default | Description |
|---|---|---|
| `--browser` | — | Use cookies from Firefox/Chrome |
| `--quality` | `best` | `best`, `worst`, or a height like `720` |
| `--output` | `./downloads` | Output directory |
| `--clear-cache` | — | Clear cached session and re-login |

## How It Works

1. **Auth** — Extracts session cookies from your browser or logs in via credentials
2. **Extract** — Fetches the post page and finds the HLS (`.m3u8`) or MP4 stream URL
3. **Download** — Uses `yt-dlp` + `ffmpeg` to download and merge the stream into an MP4

## Project Structure

```
fansone-downloader/
├── src/
│   ├── auth.py         # Cookie/login handling
│   ├── extractor.py    # Stream URL extraction
│   └── downloader.py   # yt-dlp download wrapper
├── main.py             # CLI entry point
├── requirements.txt
├── .env.example
└── CLAUDE.md
```
