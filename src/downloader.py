"""
Core download logic using yt-dlp.

yt-dlp handles:
  - HLS stream merging (ffmpeg)
  - progress display
  - retries
  - output naming
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import yt_dlp

from .extractor import extract_stream_url


DEFAULT_OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./downloads")
DEFAULT_QUALITY = os.getenv("QUALITY", "best")


def _build_ydl_opts(output_dir: str, quality: str, cookies: dict) -> dict:
    """Build yt-dlp options dict."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    format_selector = "bestvideo+bestaudio/best"
    if quality != "best":
        if quality == "worst":
            format_selector = "worstvideo+worstaudio/worst"
        else:
            # e.g. quality="720" → prefer ≤720p
            format_selector = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]/best"

    return {
        "format": format_selector,
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) "
                "Gecko/20100101 Firefox/122.0"
            ),
            "Referer": "https://fansone.co",
        },
        # Inject session cookies so yt-dlp can access protected streams
        "http_headers": {
            "Cookie": "; ".join(f"{k}={v}" for k, v in cookies.items()),
        },
        "retries": 5,
        "fragment_retries": 5,
        "ignoreerrors": False,
        "quiet": False,
        "no_warnings": False,
    }


def download(
    url: str,
    cookies: dict,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    quality: str = DEFAULT_QUALITY,
    stream_url: Optional[str] = None,
) -> None:
    """
    Download a fansone.co video.

    Args:
        url:        The fansone.co post URL.
        cookies:    Authenticated session cookies.
        output_dir: Directory to save the file.
        quality:    'best', 'worst', or a height like '720'.
        stream_url: If already extracted, skip re-extraction.
    """
    target_url = stream_url

    if not target_url:
        print(f"[*] Extracting stream URL from: {url}")
        target_url = extract_stream_url(url, cookies)

    if not target_url:
        # Fall back: let yt-dlp try the page URL directly with cookies
        print("[!] Could not extract stream URL directly. Trying yt-dlp on the page URL...")
        target_url = url

    print(f"[*] Downloading: {target_url}")
    opts = _build_ydl_opts(output_dir, quality, cookies)

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([target_url])

    print(f"[+] Done. Saved to: {output_dir}")
