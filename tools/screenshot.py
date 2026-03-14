"""
Tool: screenshot.py
Purpose: Capture a full-page or viewport screenshot of a local page using Playwright.
Usage: python3 tools/screenshot.py <url> <output_path> [--full-page] [--clip x,y,w,h] [--width 1440] [--height 900]
"""

import asyncio
import argparse
import sys
from pathlib import Path
from playwright.async_api import async_playwright


async def capture(url: str, output: str, full_page: bool, clip, width: int, height: int):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        await page.goto(url, wait_until="networkidle")
        kwargs = {"path": output, "full_page": full_page}
        if clip:
            kwargs["clip"] = clip
            kwargs["full_page"] = False
        await page.screenshot(**kwargs)
        await browser.close()
        print(f"Screenshot saved: {output}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output")
    parser.add_argument("--full-page", action="store_true", default=False)
    parser.add_argument("--clip", help="x,y,width,height", default=None)
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=900)
    args = parser.parse_args()

    clip = None
    if args.clip:
        x, y, w, h = map(int, args.clip.split(","))
        clip = {"x": x, "y": y, "width": w, "height": h}

    asyncio.run(capture(args.url, args.output, args.full_page, clip, args.width, args.height))


if __name__ == "__main__":
    main()
