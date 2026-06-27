# Design spec — Search syntax cheat sheet

Status: Production draft

## High-level overview
One-page US Letter portrait DOCX, editable, built with python-docx. Uses official BCBSKS primary logo at 2 inches wide on white.

## Architectural diagram concepts
Top band: title and logo. Middle: shaded scope panel plus three-column search table. Bottom: shared-mailbox steps, tips, and human-review placeholders.

## Step-by-step setup
Run `python3 build/build_asset_05_search_cheat_sheet.py`. The script creates the DOCX and validation reports under `build/output/supplemental-assets/`.

## Common Gotchas
- Do not convert the page to a single image.
- Use monospace only for search expressions.
- Keep search expressions selectable.
- Do not claim accessibility compliance until human review is complete.
