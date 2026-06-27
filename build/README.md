# Classic Outlook detailed build plan build

Builds the authoritative Markdown source into a real Word `.docx` and creates validation reports.

## macOS setup

```bash
python3 -m venv ~/Documents/Classic-Outlook-Docs-venv
source ~/Documents/Classic-Outlook-Docs-venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r build/requirements.txt
python3 build/build_classic_outlook_detailed_plan.py
```

## Outputs

Outputs are written to `build/output/`:

- `Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_v1.0.docx`
- build report
- source inventory CSV
- validation report
- unresolved-items report

The DOCX is generated locally from `02. Detailed build plan.md` with `python-docx` when available. It is not a Markdown placeholder. Generated `.docx` files are intentionally ignored by Git because binary files are not supported for review.
