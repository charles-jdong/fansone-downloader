#!/usr/bin/env python3
"""
fansone-downloader — CLI entry point

Usage:
    python main.py <url> [options]

Examples:
    # Use cookies from Firefox (must be logged in to fansone.co in Firefox)
    python main.py https://fansone.co/post/xxxxx --browser firefox

    # Use .env credentials (FANSONE_EMAIL + FANSONE_PASSWORD)
    python main.py https://fansone.co/post/xxxxx

    # Specify quality and output directory
    python main.py https://fansone.co/post/xxxxx --quality 720 --output ./my-downloads

    # Clear cached cookies and re-login
    python main.py https://fansone.co/post/xxxxx --clear-cache
"""

from __future__ import annotations

import argparse
import sys

from rich.console import Console
from rich.panel import Panel

from src.auth import clear_cookie_cache, load_cookies
from src.downloader import download

console = Console()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fansone-downloader",
        description="Download videos from fansone.co",
    )
    parser.add_argument("url", help="fansone.co post URL to download")
    parser.add_argument(
        "--browser",
        choices=["firefox", "chrome", "chromium", "edge"],
        default=None,
        help="Extract cookies from this browser (must be logged in)",
    )
    parser.add_argument(
        "--quality",
        default="best",
        help="Video quality: best (default), worst, or height like 720",
    )
    parser.add_argument(
        "--output",
        default="./downloads",
        help="Output directory (default: ./downloads)",
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear cached session cookies and re-authenticate",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    console.print(Panel("[bold cyan]fansone-downloader[/bold cyan]", expand=False))

    if args.clear_cache:
        clear_cookie_cache()
        console.print("[yellow]Cookie cache cleared.[/yellow]")

    try:
        console.print("[*] Loading authentication cookies...")
        cookies = load_cookies(browser=args.browser)
        console.print(f"[green]✓[/green] Cookies loaded ({len(cookies)} entries)")
    except Exception as exc:
        console.print(f"[red]Auth error:[/red] {exc}")
        return 1

    try:
        download(
            url=args.url,
            cookies=cookies,
            output_dir=args.output,
            quality=args.quality,
        )
    except Exception as exc:
        console.print(f"[red]Download error:[/red] {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
