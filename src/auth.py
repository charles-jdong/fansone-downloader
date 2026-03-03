"""
Authentication and cookie handling for fansone.co.

Supports two modes:
  1. browser_cookie3 — grab cookies directly from Firefox/Chrome (no password needed)
  2. .env credentials — login via POST request and persist session cookies
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://fansone.co"
COOKIE_CACHE = Path(".cookies.json")


def get_cookies_from_browser(browser: str = "firefox") -> dict:
    """Extract fansone.co cookies from an installed browser session."""
    try:
        import browser_cookie3

        loader = getattr(browser_cookie3, browser, None)
        if loader is None:
            raise ValueError(f"Unsupported browser: {browser}. Use 'firefox' or 'chrome'.")

        jar = loader(domain_name="fansone.co")
        cookies = {c.name: c.value for c in jar}
        if not cookies:
            raise RuntimeError(f"No fansone.co cookies found in {browser}. Are you logged in?")
        return cookies
    except ImportError:
        raise ImportError("browser-cookie3 not installed. Run: pip install browser-cookie3")


def login_with_credentials() -> dict:
    """Login using FANSONE_EMAIL / FANSONE_PASSWORD from .env and return cookies."""
    email = os.getenv("FANSONE_EMAIL")
    password = os.getenv("FANSONE_PASSWORD")

    if not email or not password:
        raise ValueError("FANSONE_EMAIL and FANSONE_PASSWORD must be set in .env")

    session = requests.Session()

    # Step 1: get CSRF token from login page
    resp = session.get(f"{BASE_URL}/login", timeout=15)
    resp.raise_for_status()

    # Parse CSRF token from HTML (common pattern for Laravel/PHP apps)
    csrf_token = _extract_csrf(resp.text)

    # Step 2: POST credentials
    payload = {
        "_token": csrf_token,
        "email": email,
        "password": password,
    }
    resp = session.post(f"{BASE_URL}/login", data=payload, timeout=15, allow_redirects=True)
    resp.raise_for_status()

    cookies = dict(session.cookies)
    if not cookies:
        raise RuntimeError("Login failed: no session cookies returned. Check your credentials.")

    # Cache for reuse
    COOKIE_CACHE.write_text(json.dumps(cookies), encoding="utf-8")
    return cookies


def load_cookies(browser: Optional[str] = None) -> dict:
    """
    Load cookies using the best available method:
      1. Cached cookies from a previous login (if present)
      2. Browser cookies (if --browser flag provided)
      3. .env credentials login
    """
    if COOKIE_CACHE.exists():
        cookies = json.loads(COOKIE_CACHE.read_text(encoding="utf-8"))
        if cookies:
            return cookies

    if browser:
        return get_cookies_from_browser(browser)

    return login_with_credentials()


def clear_cookie_cache() -> None:
    if COOKIE_CACHE.exists():
        COOKIE_CACHE.unlink()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_csrf(html: str) -> str:
    """Extract CSRF token from a meta tag or hidden input."""
    import re

    # <meta name="csrf-token" content="...">
    m = re.search(r'<meta[^>]+name=["\']csrf-token["\'][^>]+content=["\']([^"\']+)["\']', html)
    if m:
        return m.group(1)

    # <input type="hidden" name="_token" value="...">
    m = re.search(r'<input[^>]+name=["\']_token["\'][^>]+value=["\']([^"\']+)["\']', html)
    if m:
        return m.group(1)

    return ""
