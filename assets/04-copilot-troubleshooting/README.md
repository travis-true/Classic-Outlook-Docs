# Asset 04 — Copilot troubleshooting card

Status: Production draft

## Build locally on macOS

Paste this into a fresh Terminal window while you are in your home directory:

```bash
cd "$HOME" || exit 1

REPO="$HOME/Documents/Classic-Outlook-Docs"
VENV="$HOME/Documents/Classic-Outlook-Docs-venv"

if [ ! -d "$REPO/.git" ]; then
  git clone https://github.com/travis-true/Classic-Outlook-Docs.git "$REPO"
fi

cd "$REPO" || exit 1

git switch main
git pull --ff-only origin main

python3 -m venv "$VENV"
source "$VENV/bin/activate"

python3 -m pip install --upgrade pip
python3 -m pip install -r "$REPO/build/requirements.txt"

python3 "$REPO/build/build_asset_04_copilot_troubleshooting.py"

BUILD_STATUS=$?

echo
echo "BUILD EXIT CODE: $BUILD_STATUS"

if [ "$BUILD_STATUS" -ne 0 ]; then
  echo "BUILD FAILED"
  exit "$BUILD_STATUS"
fi

find "$REPO/build/output/supplemental-assets/04-copilot-troubleshooting" -maxdepth 3 -type f -print

open "$REPO/build/output/supplemental-assets/04-copilot-troubleshooting"
```
