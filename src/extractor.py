"""
Video stream URL extractor for fansone.co.

Strategy:
  1. Fetch the post/video page with authenticated cookies.
  2. Look for HLS (.m3u8) or MP4 source URLs in the HTML or JSON response.
  3. Return the best-quality stream URL.
"""

from __future__ import annotations

import re
from typing import Optional

import requests


BASE_URL = "https://fansone.co"

# Patterns to find stream URLs in page source
_M3U8_PATTERN = re.compile(r'https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*')
_MP4_PATTERN = re.compile(r'https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*')
_SOURCE_PATTERN = re.compile(r'"source"\s*:\s*"([^"]+)"')
_VIDEO_SRC_PATTERN = re.compile(r'<source[^>]+src=["\']([^"\']+)["\']')


def extract_stream_url(page_url: str, cookies: dict) -> Optional[str]:
    """
    Fetch a fansone.co video page and extract the stream URL.

    Returns the stream URL string, or None if not found.
    """
    session = requests.Session()
    session.cookies.update(cookies)
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) "
            "Gecko/20100101 Firefox/122.0"
        ),
        "Referer": BASE_URL,
    })

    resp = session.get(page_url, timeout=20)
    resp.raise_for_status()
    html = resp.text

    # Priority: m3u8 > source JSON > <source> tag > mp4
    for pattern in (_M3U8_PATTERN, _SOURCE_PATTERN, _VIDEO_SRC_PATTERN, _MP4_PATTERN):
        m = pattern.search(html)
        if m:
            url = m.group(1) if pattern.groups else m.group(0)
            url = url.strip().replace("\\u0026", "&").replace("\\/", "/")
            return url

    return None


def extract_post_id(page_url: str) -> Optional[str]:
    """Extract post ID from a fansone.co URL."""
    m = re.search(r"/post(?:s)?/([a-zA-Z0-9_-]+)", page_url)
    return m.group(1) if m else None
