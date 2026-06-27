# Video production standards

Status: Production draft

## High-level overview

Create six short, task-first Classic Outlook videos for BCBSKS employees. Do not create MP4 files from this package. The files are production inputs for a human recording and editing workflow.

## Architectural diagram concepts

Source guide content flows into script, storyboard, shot list, captions, transcript, audio-description notes and title/end-card specs. Human capture then replaces synthetic storyboard mockups before publication.

## Step-by-step setup

1. Build the package with `python3 build/build_asset_07_video_package.py`.
2. Review scripts and shot lists with IT Training and Outlook support.
3. Replace each synthetic storyboard frame with an approved capture.
4. Record at 1920 × 1080, 30 fps, 16:9.
5. Time captions against the recorded video before publication.

## Common Gotchas

- Do not use background music during instructions.
- Do not rely on cursor movement alone.
- Use no more than three callouts per scene.
- Use fictional dummy data only.
- Do not label captions final until timed against the recorded video.
