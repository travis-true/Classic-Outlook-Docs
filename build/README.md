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

## Employee-facing guide build

```bash
python3 build/build_classic_outlook_employee_guide.py
```

The employee-facing build creates:

- `docs/training/Take-Control-of-Your-Inbox_Classic-Outlook-for-Windows.md`
- `build/output/Take-Control-of-Your-Inbox_Classic-Outlook-for-Windows_v1.0.docx`
- build, validation, unresolved-items, and source-inventory reports

The generated DOCX is a real editable OOXML Word document. It is generated locally and uploaded by GitHub Actions, but it is not committed because binary files are not supported for review. When `python-docx` is available, the builder uses it for richer Word styling. When local dependency installation is blocked, the builder falls back to a deterministic standard-library OOXML writer so the artifact still builds.
