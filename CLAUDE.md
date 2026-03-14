# NØ QUIT Performance — Project Instructions

## Project Overview

Static HTML storefront for **NØ QUIT Performance**, a phenylcapsaicin supplement brand. No backend, no database, no build process — just HTML, CSS, vanilla JS served directly.

**Product:** NØ QUIT Phenylcapsaicin Capsules (60 capsules, 30 servings, 2.5mg phenylcapsaicin per serving)
**Tagline:** "Finish Strong. Recover Ready."

## Tech Stack

- **HTML5** — 5 static pages (index, product, about, science, faq)
- **CSS3** — Custom design system with CSS variables, no framework
- **Vanilla JavaScript** — No frameworks, shared `main.js` across all pages
- **Python 3** — Single screenshot utility using Playwright
- **Fonts** — Google Fonts CDN (Barlow, Barlow Condensed, DM Serif Display)

## Directory Layout

```
storefront/           # The website (has its own git repo)
├── index.html        # Homepage
├── product.html      # Product detail page
├── about.html        # Brand story
├── science.html      # Research & science
├── faq.html          # FAQ & support
├── styles.css        # Full design system (1,220 lines)
├── js/main.js        # Shared JS (352 lines)
├── images/           # Product & content images
└── video/            # Bottle animation video

Brand_assets/         # Brand materials, logos, product images
tools/                # Python scripts
  └── screenshot.py   # Playwright screenshot tool
.tmp/                 # Temporary files (disposable, regenerated as needed)
workflows/            # Markdown SOPs (to be created as needed)
```

## Design System

The CSS design system in `storefront/styles.css` defines everything. Respect these tokens when making changes:

- **Colors:** Black (#080808), White (#EDE9E3), Steel accent (#6E8494), surface levels (#101010 → #252525)
- **Typography:** Barlow Condensed for headings, Barlow for body, DM Serif Display for editorial accents
- **Spacing:** 10-level scale from 6px to 192px
- **Layout:** Max-width 1320px, responsive breakpoints at 1100px, 900px, 768px, 480px
- **Motion:** Custom cubic-bezier easing, transitions from 0.18s to 0.9s

## Available Tools

**`tools/screenshot.py`** — Capture full-page or viewport screenshots using Playwright
```bash
python3 tools/screenshot.py <url> <output_path> [--full-page] [--clip x,y,w,h] [--width 1440] [--height 900]
```
Requires: `pip install playwright && playwright install chromium`

## JS Features (in main.js)

- Header scroll state (background on scroll)
- Cart drawer with add/remove/quantity
- Mobile hamburger navigation
- Scroll reveal animations (IntersectionObserver)
- Video play/pause on viewport visibility
- Accordion expand/collapse
- Purchase option toggle (subscribe vs one-time)
- Product image gallery with thumbnail switching
- Email form submission feedback

## How to Preview

Open any HTML file directly in a browser, or use a local server:
```bash
cd storefront
python3 -m http.server 8000
# Visit http://localhost:8000
```

## WAT Framework

This project uses the **WAT framework** (Workflows, Agents, Tools) for agent-assisted work.

**Workflows** — Markdown SOPs in `workflows/` defining objectives, inputs, tools to use, expected outputs, and edge cases. Don't create or overwrite workflows without asking.

**Agents** — You (Claude). Read the relevant workflow, run tools in sequence, handle failures, ask clarifying questions when needed. Look for existing tools before building new ones.

**Tools** — Python scripts in `tools/` for deterministic execution. Consistent, testable, fast.

**Why:** When AI handles every step directly, accuracy compounds downward. Offloading execution to scripts keeps accuracy high.

## When Things Break

1. Read the full error message and trace
2. Fix the script and retest (check with me before re-running paid API calls)
3. Document what you learned in the relevant workflow
4. Move on with a more robust system

## Key Rules

- Final deliverables go to cloud services (Google Sheets, Slides, etc.), not local files
- Everything in `.tmp/` is disposable
- Don't store secrets outside `.env`
- Don't create or overwrite workflows without asking
- Stay pragmatic. Stay reliable. Keep learning.
