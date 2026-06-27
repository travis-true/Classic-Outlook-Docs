# Asset 01 — Classic Outlook Task Map Title Banner

Status: Production draft

This folder contains the editable SVG source and icon source for the Classic Outlook Task Map title banner. PNG exports are generated locally and in the GitHub Actions artifact, but are not committed because repository review does not support binary files.

## macOS fresh-Terminal build

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

python3 "$REPO/build/build_title_banners.py" --asset 01

BUILD_STATUS=$?

echo
echo "BUILD EXIT CODE: $BUILD_STATUS"

if [ "$BUILD_STATUS" -ne 0 ]; then
  echo "BUILD FAILED"
  exit "$BUILD_STATUS"
fi

find "$REPO/build/output/title-banners" -type f -print | sort

open "$REPO/build/output/title-banners"
```
