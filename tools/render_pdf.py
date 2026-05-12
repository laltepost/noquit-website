"""
Tool: render_pdf.py
Purpose: Render an HTML page to PDF using Playwright/Chromium. Uses page CSS
for size/margins (the source defines `@page { size: letter; margin: 0 }`).

Usage:
  python3 tools/render_pdf.py <url> <output_path> [--format letter|a4]

Notes:
- Waits for `networkidle` plus document.fonts.ready so web fonts render
  consistently before the PDF is produced.
- prefers-color-scheme is set to "light" so the brand-manual paper background
  renders as designed regardless of the OS theme.
"""

import argparse
import asyncio
import sys
from playwright.async_api import async_playwright


async def render(url: str, output: str, fmt: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(color_scheme="light")
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.emulate_media(media="print")
        await page.pdf(
            path=output,
            format=fmt,
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
        print(f"PDF saved: {output}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output")
    parser.add_argument("--format", default="letter", choices=["letter", "a4"])
    args = parser.parse_args()
    asyncio.run(render(args.url, args.output, args.format))


if __name__ == "__main__":
    main()
