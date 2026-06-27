# Codex Master Prompt — Classic Outlook Detailed Guide Build Plan

## Mission

Act as a senior instructional designer, technical writer, Microsoft Outlook training architect, accessibility specialist, information architect, Word document engineer and BCBSKS document designer.

Create the **detailed guide build plan** for:

**Take Control of Your Inbox: Classic Outlook for Windows**

Use the public GitHub repository:

- Repository: `https://github.com/travis-true/Classic-Outlook-Docs`
- Clone URL: `https://github.com/travis-true/Classic-Outlook-Docs.git`
- Default branch: `main`

Do not return only a chat outline. Inspect the repository, create the source document, implement a deterministic Word build, run it, validate the output and prepare the changes for a pull request.

This task creates deliverable 1 only:

**Detailed guide build plan**

Do not create the page-by-page plan, complete copy deck, screenshot set or final employee guide during this task. Define how those later deliverables will be built.

---

# 1. Repository handling

First determine whether the workspace is already the repository.

When already in the repository, run:

```bash
git remote -v
git branch --show-current
git rev-parse HEAD
git status --short
```

Confirm that the remote references `travis-true/Classic-Outlook-Docs`.

Use the existing workspace. Do not create a nested clone. Do not reset, clean, discard or overwrite unrelated user changes.

When the repository is not already open:

```bash
git clone --depth 1 --branch main https://github.com/travis-true/Classic-Outlook-Docs.git
cd Classic-Outlook-Docs
```

The repository is public. Do not request credentials merely to clone it.

Create a working branch when supported:

```bash
git switch -c codex/build-classic-outlook-detailed-plan
```

Record the repository URL, branch, commit SHA, working-tree status, build time, operating system, Python version and dependencies.

---

# 2. Required sources

Recursively locate these files using Unicode-normalized and case-insensitive filename matching:

1. `01. Locked scope for Guide 1.md`
2. `BCBSKS-ID-Prompt-Guide-v4.0.md`
3. `BCBSKS_Master_Brand_Kit.md`

Accept download suffixes such as `(1)` or `(4)` only when the base filename and contents clearly match.

Exclude `.git`, virtual environments, caches, generated output and external symlinks from source discovery.

If a required source is missing:

1. Write `build/output/BUILD_BLOCKED.md`.
2. List the missing source and searched paths.
3. Stop with a nonzero exit code.
4. Do not fabricate missing requirements.

---

# 3. Authority order

Resolve conflicts in this order:

1. `01. Locked scope for Guide 1.md`
   - Controls title, audience, environment, exact scope, core workflow, recurring reminders, deliverable sequence, screenshot placeholders and platform markers.

2. `BCBSKS_Master_Brand_Kit.md`
   - Controls current colors, typography, logo, disclosure, Plain Talk, corporate writing style and document design.

3. `BCBSKS-ID-Prompt-Guide-v4.0.md`
   - Controls R-C-A-O-U, F-S-D, UDL, cognitive load, accessibility, AI limitations, human review gates and QA.

When standards conflict, use the current Master Brand Kit values. Do not blend conflicting palettes.

---

# 4. Locked project context

## Title

**Take Control of Your Inbox: Classic Outlook for Windows**

## Audience

Sales Account Representatives and Sales Account Associates using company-managed Windows laptops and work Microsoft 365 accounts.

## Environment assumptions

- Microsoft 365 Premium
- Current supported Classic Outlook desktop application
- Microsoft 365 Copilot licensed for all users
- Work accounts only
- Email-related calendar follow-up only
- Shared mailboxes included
- General safe-use language
- Support and policy placeholders included

The exact Microsoft 365 Apps update channel is unknown.

Use this note when needed:

> Your screen may look slightly different depending on your Microsoft 365 update version.

Do not invent an update channel, Outlook build, Windows version, tenant setting, support path, policy link, permission, feature rollout or approval.

---

# 5. Locked content scope

The detailed plan must account for all 26 topics:

1. Identify Classic Outlook and understand the layout
2. Read, reply, reply all and forward
3. Create and send email
4. Attach files and share cloud links
5. Search for messages, people and attachments
6. Decide whether an email needs action
7. Flag messages and set reminders
8. Add and use categories
9. Create folders and move messages
10. Archive and delete messages
11. Use Focused Inbox
12. Create and manage rules
13. Use follow-up calendar cues
14. Create appointments or meetings from email
15. Configure and use automatic replies
16. Create and manage signatures
17. Open and use shared mailboxes
18. Summarize email threads with Copilot
19. Identify decisions, action items, owners and deadlines
20. Draft replies with Copilot
21. Rewrite for clarity, tone or length
22. Use Coaching by Copilot where available
23. Create a meeting from an email with Copilot where available
24. Review Copilot output before sending
25. Troubleshoot missing commands or unavailable features
26. Get help and use related resources

Do not remove, add or silently combine away topics. Closely related topics may share a section, but every topic must have one primary mapping in the scope matrix.

---

# 6. Locked workflow and messages

Preserve:

**Email → Decide → Make visible → Follow through**

Reinforce:

- **Does this need action from me?**
- **What is the next step?**
- **Where will I make it visible?**

Preserve exactly:

**Copilot starts the draft. You finish the message.**

Explain where these messages recur without becoming repetitive.

---

# 7. Deliverable sequence

Preserve this sequence:

1. Detailed guide build plan
2. Page-by-page copy plan
3. Complete copy deck
4. Screenshot capture and annotation plan
5. Platform-difference notes for future master-guide integration
6. Final Word document, when requested

Create deliverable 1 only. Define the inputs, outputs, dependencies and review gates for deliverables 2–6.

---

# 8. Required outputs

Create:

```text
02. Detailed build plan.md
build/build_classic_outlook_detailed_plan.py
build/requirements.txt
build/README.md
build/output/Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_v1.0.docx
build/output/Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_Build-Report_v1.0.md
build/output/Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_Source-Inventory_v1.0.csv
build/output/Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_Validation_v1.0.md
build/output/Take-Control-of-Your-Inbox_Classic-Outlook_Detailed-Build-Plan_Unresolved-Items_v1.0.md
```

`02. Detailed build plan.md` is the authoritative, reviewable source.

Generate a real `.docx` with `python-docx`. Do not create `.docx.md`, rename Markdown as DOCX or substitute a placeholder.

A PDF layout preview is optional only when a reliable local converter is available. Do not claim a PDF is final or accessible without validation.

---

# 9. Required build-plan sections

## 1. Asset overview

Include:

- Asset title and subtitle recommendation
- Asset type
- Primary and secondary audiences
- Primary platform
- Device context
- Account scope
- Publishing format
- Estimated final-guide length range
- Estimated use pattern
- Owner
- Version
- Status
- Last reviewed placeholder
- Support placeholder
- Feedback placeholder
- Related training
- Related platform guides
- Classification

Do not choose a final page count without explaining the task-based estimate.

## 2. Purpose

Explain the workplace performance problem. The final guide is a task-based reference, not a book employees must read linearly.

## 3. Performance outcomes

Write observable, task-focused outcomes based only on the locked scope.

## 4. Core workflow

Explain how the four-part workflow and three recurring questions organize the guide.

## 5. Audience and use context

Address experience range, email volume, shared-mailbox use, keyboard-and-mouse workflow, managed Windows devices, work accounts, fast task retrieval, accessibility needs and use while Outlook is open.

## 6. Environment assumptions and validation needs

Separate:

- Locked assumptions
- Technical validation needs
- Policy validation needs
- Availability-dependent features
- Permission-dependent features
- Configuration-dependent features

Include the approved update-version note.

## 7. Scope boundaries

Create:

- In scope
- Out of scope
- Redirect/handoff rules
- Dependencies on later deliverables

Do not expand into general Windows support, full calendar administration, mailbox administration, records policy, security policy or unrelated Microsoft 365 applications.

## 8. Information architecture

Propose and justify a task-first section sequence. A recommended structure is:

1. Start here and identify Classic Outlook
2. Read and respond
3. Create and send
4. Attach and share
5. Decide and make follow-up visible
6. Organize and clean up
7. Search
8. Use calendar follow-up
9. Configure Outlook
10. Work in shared mailboxes
11. Use Copilot
12. Troubleshoot and get help
13. Platform comparison and final reminders

Refine only when the locked scope supports a better structure.

## 9. Scope-to-section matrix

Create a table with:

- Scope number
- Locked topic
- Proposed guide section
- Proposed task title
- Content treatment
- Screenshot need
- Platform marker
- Validation need
- Cross-reference

All topics 1–26 must appear exactly once as primary mappings.

## 10. Reusable task-page blueprint

Define required and optional components:

- Task title
- When to use
- Before you begin
- Numbered steps
- Success check
- Decision cue
- Warning or limitation
- Platform marker
- Screenshot placeholder
- Alt-text draft
- Related task
- Get help
- Footer/version

## 11. Guide-section blueprint

For each major section, define:

- Purpose
- Included tasks
- Entry point
- Key decision
- Examples
- Screenshot needs
- Copilot/shared-mailbox considerations
- Platform differences
- Support handoff
- Estimated page range

## 12. Page-budget model

Estimate, do not fabricate, a page range for:

- Front matter
- Start-here content
- Task pages
- Decision/comparison pages
- Troubleshooting
- Index/glossary
- Support/final reminder
- Screenshot expansion allowance

Explain the assumptions.

## 13. Navigation and findability

Plan:

- Automatic table of contents
- Searchable task titles
- Descriptive headings
- PDF bookmarks
- Cross-references
- Related-task links
- Task finder/index
- Alternate search terms
- Headers/footers
- SharePoint metadata

## 14. Screenshot framework

Do not create screenshots in this task.

Every future placeholder must define:

- Screenshot ID
- Exact screen and action
- Recommended crop
- Context to retain
- Maximum three callouts
- Action-focused callout labels
- Alt-text draft
- Sensitive information to replace
- Placement
- Feature-validation status
- Replacement trigger

Do not fabricate interfaces or expose real employee, customer, producer, member, account or mailbox data.

## 15. Screenshot annotation standard

Use:

- Bluejay `#41B6E6` shapes
- White callout text
- Midnight `#002855` supporting labels
- Numbered circles for sequences
- High-contrast outlines
- Maximum three callouts
- Three to six words per label
- One action per callout
- No crossing leader lines
- No color-only meaning
- No covering interface labels

Prefer labels such as:

- Select the File tab
- Open Rules and Alerts
- Confirm the From address
- Choose Automatic Replies
- Review the Copilot draft

Avoid vague labels such as “Click here,” “This button” or “Look here.”

## 16. Fictional-data standard

Plan a consistent dummy-data package using:

- Nonfunctional `example.com` addresses
- Fictional employees and organizations
- Low-risk subjects and files
- No real signatures
- No real mailbox content
- No member, customer, producer, account, claim or policy information
- No personal notifications
- No verification codes
- No confidential links

## 17. Platform-difference system

Use these exact markers:

- **Same on most platforms**
- **Different in New Outlook**
- **Different on the web**
- **Different on iPad**
- **Not available**
- **Availability may depend on licensing or configuration**

Define when each appears, its visual/accessibility treatment and how it supports future master-guide assembly.

Do not imply feature parity without validation.

## 18. Copilot content model

Plan consistent treatment for:

- Thread summaries
- Decisions
- Action items
- Owners
- Deadlines
- Draft replies
- Rewriting for tone, clarity or length
- Coaching
- Creating meetings where available
- Final review before sending

Require human review of accuracy, sources, recipients, From address, names, owners, dates, deadlines, tone, completeness, attachments, links, permissions, sensitive information and final wording.

Do not describe Copilot as authoritative.

## 19. Shared-mailbox model

Plan:

- Permission prerequisites
- Opening/adding the mailbox
- Switching mailboxes
- Confirming active mailbox
- Confirming From address
- Reviewing Shared Sent
- Ownership/status coordination
- Search
- Everyday use versus administration
- Permission-dependent behavior
- Escalation

Do not suggest sharing credentials or signing in as the mailbox.

## 20. Decision-support model

Map the core questions to:

- Reply
- Reply All
- Forward
- Flag
- Reminder
- Category
- Folder
- Rule
- Appointment
- Meeting
- Shared-mailbox status
- Copilot support
- Closing the loop

## 21. UDL and accessibility plan

### Engagement

- Immediate relevance
- Clear purpose
- Predictable structure
- Low-friction task entry
- Self-checks
- No unnecessary time pressure

### Representation

- Plain language
- Text plus visuals
- Descriptive headings
- Real tables
- Alt text
- Icons with labels
- Consistent callouts
- Defined acronyms
- No sensory-dependent instructions

### Action and expression

- Keyboard and mouse support where useful
- Descriptive links
- Logical reading order
- Clear success checks
- Alternative support path
- No color-only cues

### Accessibility target

- WCAG 2.1 AA principles
- Screen-reader-compatible Word
- Minimum 11-point body text
- 4.5:1 normal-text contrast
- Accessible tables
- Real heading styles
- Real lists
- Inline images
- Alt text
- English (United States)
- Human accessibility testing required

Do not claim compliance from automation alone.

## 22. Cognitive-load rules

Include:

- One task per procedure
- Short step groups
- Progressive disclosure
- Chunked troubleshooting
- Limited callouts
- Consistent page patterns
- Clear prerequisites
- Minimal duplication
- Separate “what to do” from “why”
- Advanced exceptions outside basic flow
- Cross-references instead of repeated procedures

## 23. BCBSKS Plain Talk

Use:

- Clear over clever
- Helpful over decorative
- Human and approachable
- Warm but professional
- Sixth- to eighth-grade reading level
- Active voice
- Common words
- Short sentences
- One main idea per paragraph
- Descriptive headings
- Bullets and numbered steps
- Most important information first

Avoid justified text, dense paragraphs, unexplained acronyms, all-caps emphasis and decorative language.

## 24. Visual design system

Use the current Master Brand Kit values:

- Blue: `#005EB8`
- Midnight: `#002855`
- Bluejay: `#41B6E6`
- Sky: `#77C5D5`
- Slate gray: `#333132`
- Text gray: `#4D4D4F`
- Light gray: `#A7A9AC`
- Subtle gray: `#E6E7E8`
- White: `#FFFFFF`
- Warning red: `#C63527`, warnings only

Rules:

- Lead with blues, approved grays and white.
- Use no more than three primary colors per page when practical.
- Do not use Warning red decoratively.
- Do not rely on color alone.
- Ensure grayscale readability.
- Use white space intentionally.
- Avoid busy patterns behind text.

## 25. Typography

For training assets:

- Page titles: Georgia Bold or Arial Bold, 18–24 pt
- Section headings: Georgia Bold or Arial Bold, 12–16 pt
- Body: Arial or Arial Narrow, 11–12 pt
- Captions/table text: 9.5–10 pt minimum when unavoidable
- Sentence case
- Left alignment
- Bold for purposeful emphasis
- Limited italics

For this detailed plan:

- Title: Georgia Bold, 22 pt
- Heading 1: Georgia Bold, 16 pt
- Heading 2: Georgia Bold, 13 pt
- Body: Arial, 11 pt
- Table text: Arial, 10 pt minimum
- 1.08–1.15 line spacing
- 6 pt paragraph spacing
- No justified text

## 26. Logo and disclosure

Use only approved logo artwork found in the repository.

Do not recreate, stretch, crop, skew, recolor, rearrange or add effects.

Primary logo minimum width: 2 inches.

If no approved logo exists:

- Create an `UNBRANDED-DRAFT`.
- Insert a labeled placeholder.
- Record a publication blocker.
- Do not download or fabricate a logo.

Where required, use:

`Blue Cross and Blue Shield of Kansas is an independent licensee of the Blue Cross Blue Shield Association.`

## 27. Word engineering plan

Specify how the final guide will use:

- US Letter portrait
- Real Word styles
- Automatic table of contents
- Heading hierarchy
- Automatic page numbers
- Cross-references
- Descriptive hyperlinks
- Real bullets and numbered lists
- Real tables
- Repeated table headers
- Inline screenshots
- Alt text
- Figure captions
- Keep-with-next
- Widow/orphan control
- Page-break control
- Document properties
- English (United States)
- Accessible reading order
- PDF bookmarks
- Tagged-PDF workflow where supported

Do not use floating text boxes for essential content.

## 28. Metadata and naming

Recommend filenames and metadata for all six deliverables, source/annotated screenshots, review reports and final PDF.

Include:

- Title
- Subtitle
- Owner
- Audience
- Platform
- Version
- Status
- Last reviewed
- Next review
- Classification
- Accessibility status
- Technical-validation status
- Related resources
- Search terms
- Publication blockers

## 29. Review workflow

Define gates for:

1. Scope
2. Instructional design
3. Technical Outlook
4. Shared mailbox
5. Copilot
6. Accessibility
7. Brand and Plain Talk
8. Policy/security
9. Final production
10. Publication approval

For each, include reviewer role, evidence, status, rework path and publication impact.

Use statuses:

- Not started
- In review
- Revise
- Approved
- Blocked

Do not invent approvals.

## 30. Validation matrix

Cover:

- Scope completeness
- Technical accuracy
- Version-neutral language
- Shared-mailbox accuracy
- Copilot accuracy
- Safe-use language
- Screenshot privacy
- Callouts
- Alt text
- Plain Talk
- Reading level
- Brand colors
- Typography
- Contrast
- Headings
- Tables
- Links
- Cross-references
- Navigation
- Word accessibility
- PDF accessibility
- Metadata
- Versioning
- Support placeholders
- Platform markers
- Human approvals

## 31. Risk and dependency register

Include:

- Unknown update channel
- Interface changes
- Feature rollout differences
- Copilot licensing/configuration
- Shared-mailbox permissions
- Missing screenshots
- Missing logo
- Missing support/policy links
- Accessibility remediation
- Page-count growth
- Duplicate platform content
- Stale screenshots
- Incorrect platform comparisons

For each, include likelihood, impact, mitigation, owner, review trigger and blocker status.

## 32. Maintenance plan

Define triggers for Microsoft 365 updates, ribbon/Backstage changes, search, rules, Focused Inbox, shared mailboxes, Copilot, calendar-from-email, signatures, automatic replies, security/policy, employee feedback, accessibility findings, master-guide integration and scheduled review.

## 33. Acceptance criteria

The plan is complete only when:

- All 26 topics are mapped.
- The core workflow is preserved.
- The three questions are preserved.
- The Copilot reminder is exact.
- The six-deliverable sequence is documented.
- Assumptions are separated from validation needs.
- The update-version note appears.
- Screenshot requirements are complete.
- Platform markers match exactly.
- UDL/accessibility are integrated.
- Current brand values are used.
- Page budgeting, review gates, risk register and maintenance triggers exist.
- Markdown and real DOCX outputs exist.
- Automated validation passes.
- Human-review needs remain visible.
- No unsupported Outlook/Copilot claim is presented as verified.

## 34. Next-step handoff

End with:

**Next deliverable: Page-by-page copy plan**

List the approvals and inputs required before it begins.

---

# 10. R-C-A-O-U record

Include an appendix documenting:

- Role
- Context and audience
- Action and assets
- Output
- UDL layer

---

# 11. F-S-D record

Include:

- Format
- Style
- Design

---

# 12. Build system

Create:

```text
build/
├── build_classic_outlook_detailed_plan.py
├── requirements.txt
├── README.md
└── output/
```

Use:

```text
python-docx==1.1.2
Pillow==10.4.0
```

Run from the repository root:

```bash
python3 build/build_classic_outlook_detailed_plan.py
```

Support Python 3.9 or later.

Use `datetime.timezone.utc`, not `datetime.UTC`.

Use `python3` in macOS instructions.

Document an external virtual environment:

```bash
python3 -m venv ~/Documents/Classic-Outlook-Docs-venv
source ~/Documents/Classic-Outlook-Docs-venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r build/requirements.txt
python3 build/build_classic_outlook_detailed_plan.py
```

Exclude `.git`, `.venv`, `venv`, `env`, caches, `build/output`, temporary render folders and external symlinks from scanning.

Never call `relative_to(root)` on a path outside the repository.

---

# 13. Word specifications

Create a real DOCX with `python-docx`.

- US Letter portrait
- Margins: 0.75–1 inch
- Real styles
- Real tables
- Header rows
- Adequate cell padding
- No screenshots of tables
- Status expressed with text, not color alone
- Automatic page numbers
- Document properties
- English (United States)
- Logical reading order

Header/footer should include:

- Take Control of Your Inbox
- Classic Outlook for Windows
- Detailed build plan
- Version 1.0
- IT Training & Enablement
- Page number
- Internal-use classification
- Disclosure when required

Use an approved logo only when available.

---

# 14. Automated validation

Check:

- All required sources found
- Source hashes recorded
- All 26 topics mapped once
- Core workflow present
- Three questions present
- Copilot reminder exact
- Six deliverables in order
- Six platform markers exact
- Update-version note present
- Required sections present
- Markdown exists
- DOCX exists
- DOCX is valid OOXML
- DOCX opens with `python-docx`
- Correct page size/orientation
- Body font at least 11 pt
- Real headings/tables
- Document properties populated
- English language applied where feasible
- No `.docx.md` substitute
- No unresolved `/mnt/data/` media path
- No invented support path or approval shown as final

If a reliable renderer exists, render and inspect for blank pages, clipped tables, header/footer overlap and orphan headings. Otherwise report that render QA was unavailable.

---

# 15. Reports

Create:

## Build report

Repository information, sources, outputs, dependencies, validation, render status, logo status, placeholders, human review and rerun command.

## Source inventory

Repository-relative path, required/optional status, purpose, size, SHA-256 and use status.

## Validation report

Use:

- Pass
- Warn
- Fail
- Human review

## Unresolved-items report

Include item, source section, type, owner, required action and blocker status.

Expected unresolved items include update channel, Windows/Outlook version, support path, policy/feedback links, review dates, logo, screenshots, permissions, Copilot availability, reviewers and approval.

---

# 16. Git and pull request

Commit the Markdown source, build script, requirements, README and text reports.

The binary DOCX may remain ignored but must be generated and validated locally.

Before committing:

```bash
git status --short
git diff --check
```

Use a clear commit message:

```text
Add Classic Outlook detailed guide build plan
```

Open a pull request when supported. Include purpose, sources, deliverables, validation, blockers, build command and binary-output note.

---

# 17. Final Codex response

Report:

1. Build status
2. Repository URL
3. Branch
4. Commit SHA
5. Sources used
6. Markdown path
7. DOCX path
8. Reports
9. Validation passed
10. Warnings
11. Publication blockers
12. Human review required
13. Pull-request URL
14. Rerun command
15. Mac setup command

Do not call the plan publication-ready until technical, accessibility, brand, policy and production reviews are complete.
