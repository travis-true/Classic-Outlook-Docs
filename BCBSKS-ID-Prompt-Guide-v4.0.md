```
# Blue Cross and Blue Shield of Kansas (BCBSKS)
## ID Prompt Engineering Reference Guide
### Version 4.0 — [Department Name] Edition

**Internal Use Document**

**Purpose:** Standardized prompt engineering handbook for creating high-quality,
accessible training assets using AI assistance across all training and enablement functions.

**Document Owner:** [Your Name]  
**Last Updated:** [Date]  
**Version:** 4.0  
**Classification:** [Internal Use]

---

## 📋 Table of Contents

| § | Section | Status |
|---|---------|--------|
| **[NEW]** §0 | **BCBSKS Customization Checklist** | ⬜ Customize Me |
| ⚡ | How to Use This Guide (Right-Sizing Effort) | ✅ Ready |
| 1 | Core ID/UDL Terminology + BCBSKS Terms | ✅ Ready |
| 2 | The R-C-A-O-U Prompt Framework | ✅ Ready |
| 3 | The F-S-D Framework (+UDL) | ✅ Ready |
| 4 | Master Templates A-H (All UDL-Enhanced) | ✅ Ready |
| 4.5 | Quick-Start One-Liners (20 tasks) | ✅ Ready |
| 4.6 | AI Limitations & Human Review Gates | ✅ Ready |
| 4.7 | Prompt Chaining Workflow | ✅ Ready |
| 5 | Complete Training Asset Library (33 assets + UDL) | ✅ Ready |
| 6 | UDL Deep Dive | ✅ Ready |
| 7 | **BCBSKS Style Bible (Brand Kit Integrated)** | ⬜ CUSTOMIZED |
| 8 | Training Lifecycle Mapping | ✅ Ready |
| 9 | Best Practices (+ BCBSKS Standards) | ✅ Ready |
| 10 | Quick Reference Cards + Anti-Patterns | ✅ 🎨 Updated |
| 11 | Pre-Publish QA Checklist | ✅ Ready |

---

## §0 🔧 BCBSKS Customization Checklist

**Complete ALL items below before distributing this guide to your team.**

### 🏢 Document Identity
- [ ] Replace any remaining "[COMPANY]" placeholders with actual values
- [ ] Confirm document owner and last updated date
- [ ] Set appropriate classification level per BCBSKS policy
- [ ] Verify this version number matches current master

### 🎨 Brand Voice & Style (from BCBSKS Brand Kit)

**TONE: Plain Talk Standard**
- Conversational style for health insurance
- Clear over clever
- Helpful over decorative
- Kansas-first, local feel
- Human-first, approachable
- Community-centered language
- Warm but professional
- Structured: give people the path, why it matters, what to do next, where to get help

**READING LEVEL:**
- Target: sixth- to eighth-grade reading level
- Use common everyday words
- Avoid insurance/medical jargon when possible
- Define terms at first use
- Keep sentences short (average 15 words)
- Keep paragraphs to one main idea
- Use bullets, numbered steps, FAQs

**TYPOGRAPHY:**
- Marketing materials: Mercksen STD Extra Bold
- Letters: Georgia
- PowerPoint: Georgia Bold
- Email: Aptos
- General documents: Georgia or Arial
- Training assets: Georgia Bold or Arial Narrow

**COLOR SYSTEM (Use These Hex Codes):**
- Primary Blue: `#5E96E8` (Pantone 300 C)
- Midnight: `#002B55` (Pantone 303 C)
- Bluejay: `#41B6E6` (Pantone 298 C)
- Sky: `#77C5D3` (Pantone 630 C)
- Slate Gray: `#333132`
- Text Gray: `#4D4F4F`
- Light Gray: `#A7A8AC`
- Subtle Gray: `#E6E7E8`
- White Space: `#FFFFFF`
- Warning Red: `#C63A39` (Pantone 7626 C)

**COLOR RULES:**
- Lead with Blue, Midnight, Sky/Bluejay, or approved grays
- Maximum three colors on one piece
- Use Midnight at ≥80% tint for small text
- Use Honeybee (#FBD384), Limestone (#EFDAF9), Marigold (#FBD384), Prairie (#C6F6D3), Sunset (#FEEAA7) for accents
- Never use more than three complement colors on one piece
- Ensure contrast ratio meets WCAG AA (4.5:1+ for body text)
- Check contrast for digital applications before publishing

**LOGO USAGE:**
- Primary logo (shield + "Kansas") for most internal/external communications
- Secondary logo (stacked shields + "Kansas") for limited space
- Tertiary logo (stacked mark) for promotional items
- Minimum size: 2 inches wide
- Clear space: At least height of the Blue Cross symbol around the mark
- Safe spaces: Social media posts, email contexts, out-of-home placements
- Licensee disclosure required when company name appears
- Co-branded materials require full disclosure and relationship statement

**LOGO MISUSE TO AVOID:**
- Don't recreate or build new versions from text/symbols
- Don't stretch, compress, crop, rearrange or add effects
- Don't place on photography or low-contrast patterns
- Don't recolor symbols except through approved treatments
- Don't use outdated versions

**CORPORATE WRITING STYLE:**
- Full name: "Blue Cross and Blue Shield of Kansas" (BCBSKS)
- Acceptable: BCBSKS, Blue Cross, the Kansas company, our company
- AVOID: BCBSSKS, BlueCrossBlueShield of Kansas, Kansas Blue Cross and Blue Shield's
- Write "Blue Cross and Blue Shield" — never "Cross and Shield" alone
- Capitalize official department names when used as description
- Lowercase product names unless part of official name
- No capitalize: claim form, enrollment form, month names
- No justified margins for Plain Talk content

**HIGH-RISK TERMS (Special Handling):**
- bcbksks.com → Always lowercase
- BlueAccess® → One word; capitalize A; registered trademark on first use
- Blue365® → One word; registered trademark on first use
- BlueCard® → One word; uppercase C; registered trademark on first use
- BlueConnect → One word; no hyphen
- Coinsurance → Two words; no hyphen
- Copay/Copayment → Two words; no hyphen
- Healthcare → Two words
- Level-funded → Hyphenated
- Payer → Use payer, not payor
- Preventive → Use preventive
- Value-based → Hyphenated
- Well-being → Hyphenated

**TEMPLATE & CHANNEL SPECIFICATIONS:**
- **Letters/Correspondence:** Corporate letterhead, left-justified margin, logo placement per brand kit
- **PowerPoint:** BCBSPowerPoint template, Georgia Bold/Arial Narrow headings, default palette (Blue, Midnight, Bluejay, grays), Warning red only for warnings
- **Email:** Aptos font, subject lines specific, action-oriented
- **SharePoint:** Descriptive titles/headings, one idea per paragraph, patterned backgrounds
- **Quick Reference Guides:** One page, short sections (3-5 steps), screenshots/icons only where helpful
- **SOPs:** Purpose, audience, prerequisites, procedure, exceptions, support path
- **Job Aids:** Start with task, minimum steps, clean hierarchy, approved colors
- **Slide Decks:** One message per slide, clean hierarchy, template fonts/approved colors
- **Screenshot Guides:** Fake member-safe data, highlight only real controls, keep callouts simple

**REVIEW CONTACTS:**
- External/public comms: externalcomms@bcbks.com
- Internal questions: corpcomm@bcbks.com
- Logo/graphics: bcreative@bcbks.com
- Legal: legal.services@bcbks.com

---

## ⚡ How to Use This Guide — Right-Size Your Effort

### Three Modes of Prompting

#### 🟢 QUICK MODE — ~2 Minutes
**When:** Internal draft • Low-stakes • Exploring options • Audience = self/close colleague
→ Go to **§4.5 Quick-Start One-Liners** — copy-paste single prompt line

#### 💰️ STANDARD MODE — ~10 Minutes
**When:** Official deliverable for team/SME review • Moderate-stakes • Single-format • Known internal audience
→ Go to **§4 Master Templates A-H** — pick matching template

#### 🔴 FULL MODE — ~30+ Minutes
**When:** External-facing • Executive-visible • High-stakes (compliance, certification) • Multi-format • Diverse audience • Legal/safety required
→ **R-C-A-O-U Framework (§2)** + **Style Bible (§7)** + **QA Checklist (§11)** + SME review

---

## §1 Core ID/UDL Terminology + BCBSKS Terms

### Learning & Development Fundamentals

| Term | Full Name | When to Use |
|------|-----------|-------------|
| LO | Learning Objective | Defining outcomes |
| Bloom's Taxonomy | Remember → Understand → Apply → Analyze → Evaluate → Create | Specifying cognitive levels |
| ADDIE | Analysis, Design, Development, Implementation, Evaluation | Curriculum design |
| SAM | Successive Approximation Model | Agile projects |
| Kirkpatrick | Four-level evaluation: Reaction → Learning → Behavior → Results | Assessment design |
| TNA | Training Needs Analysis | Gap analysis |
| SME | Subject Matter Expert | Reviewer/identifier |
| CoP | Community of Practice | Ongoing support |

### ♀ UDL Terminology

| UDL Term | Definition | Prompt Usage |
|----------|-------------|--------------|
| Multiple Means of Engagement | Options for how learners get engaged | "Include engagement options" |
| Multiple Means of Representation | Content in varied formats | "Provide in ≥2 formats" |
| Multiple Means of Action & Expression | Varied ways to demonstrate knowledge | "Offer 3+ modalities" |
| Accessibility (a11y) | Design for users with disabilities | "Ensure WCAG 2.1 AA" |
| Cognitive Load Management | Not overwhelming working memory | "Chunk into segments" |
| Scaffolding | Temporary support removed as competence grows | "Worked example → guided → independent" |
| Differentiation | Tailoring instruction to diverse needs | "Provide differentiated paths" |
| Inclusive Language | Language that doesn't exclude groups | "Use they/thediverse scenarios" |

### 🏢 BCBSKS-Specific Terminology

| Term | Definition | Context |
|------|-----------|---------|
| **BCBSKS** | Blue Cross and Blue Shield of Kansas | Official organization name |
| **BlueAccess®** | Member portal/service | Registered trademark; capitalize A |
| **Blue365®** | Member platform | Registered trademark; capitalize B |
| **BlueCard®** | Member ID card | Registered trademark; capitalize C |
| **BlueConnect** | Provider portal | One word, no hyphen |
| **Coinsurance** | Insurance coverage | Two words, no hyphen |
| **Copay/Copayment** | Member cost share | Two words, no hyphen |
| **EOB** | Explanation of Benefits | Define at first use |
| **PCP** | Primary Care Physician | Define at first use |
| **PPO** | Preferred Provider Organization | Define at first use |
| **In-Network / Out-of-Network** | Network status | Define at first use |
| **Pre-authorization** | Prior approval for service | Define at first use |
| **Claim** | Request for reimbursement | Use clear definition |
| **Member** | BCBSKS member | Use consistently |
| **Provider** | Healthcare provider | Doctor, hospital, pharmacy, lab, etc. |
| **Network** | Provider network | The BCBSKS provider network |
| **Plan** | Insurance plan type | HMO, PPO, POS, etc. |

---

## §2 The R-C-A-O-U Prompt Framework

### The Formula

```
R — C — A — O — +U
```

| Letter | Meaning | What to Specify |
|--------|---------|------------------|
| **R** | Role | Who AI acts as (e.g., "Senior ID specializing in accessible learning") |
| **C** | Context & Audience | Target role, diversity profile, device/access constraints |
| **A** | Action + Assets | Task verb, source materials, UDL checkpoint requirements |
| **O** | Output Format | Structure, alt text specs, caption specs, reading level |
| **+U** | UDL Layer | Engagement options, representation formats, expression methods |

---

## §3 The F-S-D Framework (+UDL)

| Dimension | Controls | UDL Enhancement |
|-----------|----------|----------------|
| **FORMAT** | Structure, length, medium | Multi-format options, chunked segments |
| **STYLE** | Tone, voice, reading level | Plain language, culturally responsive |
| **DESIGN** | Visual hierarchy, IA, interactions | Keyboard navigable, high contrast |

### Inclusive Style Rules (BCBSKS Plain Talk Compliant)

```
INCLUSIVE STYLE RULES:
• READING LEVEL: Sixth- to eighth-grade (per BCBS Plain Talk standard)
• JARGON: Define on first use. Build running glossary.
• SENTENCES: Max 15 words avg. One idea per sentence.
• VOICE: Conversational, warm, human-first, community-centered.
• CULTURAL: Diverse names per DEI guidelines.
• NEURODIVERSITY: Clear headings. Predictable structure.
• SENSORY: Never rely on color alone to convey meaning.

COLOR RULES FOR OUTPUT:
• Primary: Blue (#5E96E8) for headers, key terms, links
• Secondary: Midnight (#002B55) for body text
• Accent: Sky (#41B6E6) for highlights, examples
• Neutral: Slate Gray (#333132) for secondary info
• Background: White (#FFFFFF) or very light gray (#F7FAFC)
• Text: Dark Gray (#2D3748) or Black (#000000)
• Accents: Warning Red (#C63A39) for critical warnings only
• Charts/Data: Blue tints at 100%, 70%, 50%, 30% with gray fallbacks
• NEVER: More than 3 colors on one piece
• CONTRAST: Ensure 4.5:1 ratio minimum for all text
```

---

## §4 Master Prompt Templates (All UDL-Enhanced)

### Template A: Full Asset Creation (UDL-Integrated)

```
ROLE: Act as [EXPERTISE] with specialization in accessible, inclusive instructional design.

ASSET TYPE: Create a [FORMAT] titled "[TITLE]".

TARGET LEARNER: [ROLE] at [LEVEL].
DIVERSITY PROFILE:
• Accessibility needs: [visual, auditory, motor, cognitive, neurodiversity]
• Device access: [desktop/mobile/offline/screen reader]
• BCBSKS context: [member? employee? public-facing? internal-only?]

SOURCE MATERIALS: Analyze [ATTACHED DOCUMENTS].

STYLE DIRECTIVES:
• Tone: [Per BCBSKS Plain Talk standard]
• Reading level: [GRADE/TIER]
• Jargon policy: [RULE]
• Colors: [Use BCBSKS palette from §7]
• Typography: [Georgia Bold/Georgia for headings, Arial/Georgia for body]

DESIGN SPECS:
• Constraints: [PAGE COUNT / WORD COUNT / DURATION]
• Structure: [X SECTIONS]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ UDL INTEGRATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❤️ ENGAGEMENT CHECKPOINTS:
☐ Choice in [aspect: path/topic/pacing]
☐ Relevance hook connecting to [healthcare context/member benefit]
☐ Self-assessment/reflection every [N] minutes
☐ Vary challenge: [foundational/standard/stretch]

🧠 REPRESENTATION CHECKPOINTS:
☐ Content in minimum [2] formats: [list]
☐ All images have meaningful alt text
☐ Key terms defined: inline + glossary
☐ Visual organizers included

✋ ACTION & EXPRESSION CHECKPOINTS:
☐ Learners can demonstrate via [N] ways
☐ Scaffolded: worked example → guided → independent
☐ Assistive technology compatibility noted

♿ ACCESSIBILITY COMPLIANCE:
☐ WCAG Level: [AA/AAA]
☐ Contrast verified (4.5:1+)
☐ Font: [Georgia Bold/Georgia] at [size]pt
☐ Caption/transcript plan
☐ Keyboard nav required
☐ Licensee disclosure if applicable

DELIVERABLE: Ready for [REVIEW TYPE]. Flag gaps [???]. Flag a11y concerns [♿].

[BCBSKS NOTE: For external-facing or compliance-related assets, ensure full licensee disclosure is present per brand guidelines.]
```

### Template B: Storyboard / Outline Generator (UDL-Aware)

```
Act as expert ID specializing in accessible e-learning for healthcare training.

Creating [FORMAT] about [TOPIC] for [AUDIENCE: members / providers / employees / agents].

OUTPUT TABLE WITH UDL COLUMNS:
┌──────┬──────────┬──────────┬────────┬────────┬────────┬────────┐
│ Mod# │ Learning │ Content  │ Activity│ UDL-     │ UDL-     │ Access │
│      │ Objective│ Summary │ Suggest│ Engage   │ Represent│ Check  │
├──────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
│      │Learners  │Key       │Interactive│Choice   │Multi-   │Alt text│Ready  │
│      │will be   │concepts, │element │of scenario│format  │ready  │
│      │able to...│steps     │         │context  │available│       │
└──────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘

UDL COLUMN GUIDANCE:
• UDL-Engage: choice/relevance/self-reflection option
• UDL-Represent: beyond just text
• Access Check: Alt text? Captions? Keyboard nav? Reading level?

ADDITIONAL PER ROW:
• Assessment Question (offer 2+ formats)
• Estimated Time (include buffer)
• Cognitive load rating: 🟢Low 🟡Medium 🔴High
```

### Template C: Scenario-Based Learning (Inclusive Scenarios)

```
Act as scenario design specialist with focus on inclusive experiential learning for healthcare training.

Draft scenarios on [TOPIC] for [AUDIENCE: members / providers / employees].

STRUCTURE (UDL-ENHANCED):

1. SETUP:
   • Characters: Diverse representation (per BCBSKS DEI guidelines)
   • Environment: Clinical/office setting noted
   • Stakes: Real-world impact on patient care, member experience, business outcomes

2. CHALLENGE:
   • Problem in [TEXT] + [VISUAL] format
   • Red herrings clearly distinguishable
   • NO sensory-dependent cues ("you hear...", "notice the color...")
   • Realistic clinical context

3. DECISION POINT:
   • 3 options with consequence preview
   • Equally accessible (no ability-dependent advantage)
   - Option A: [clinical decision]
   - Option B: [administrative decision]
   - Option C: [patient communication]

4. CONSEQUENCES:
   • Written summary + visual impact indicator
   - Impact on: [patient safety / member satisfaction / operational efficiency]
   - "What this means for YOU as a [role]"

5. DEBRIEF:
   • Principle explained 3 ways: clinical / plain-language analogy / regulatory requirement
   • Self-reflection prompt
   - "How would you apply this with your next [patient type]?"

INCLUSIVITY CHECKLIST:
☐ Diverse characters (per BCBSKS standards)
☐ Setting access barriers noted realistically
☐ Options don't privilege one ability
☐ Feedback constructive, supportive
☐ Extension activity for advanced learners
☐ Support resource for struggling learners
☐ Compliance note if applicable
```

### Template D: Job Aid / Accessible QRG

```
Act as Technical Writer specializing in accessible performance support materials for healthcare.

Convert manual into UDL-compliant QRG.

ACCESSIBLE LAYOUT:
┌────────────────────────────────────────────┐
│ HEADER: Title (18pt+) + When to Use + Prereqs│
│        Available formats: 📄 💻 🔊 📱              │
├────────────────────────────────────────────┤
│ BODY — MULTI-FORMAT OPTIONS:               │
│ OPTION A: Step-by-step (linear, numbered)  │
│ OPTION B: Flowchart (visual, high contrast) │
│ OPTION C: Video/GIF walkthrough + captions  │
│ [SCREENSHOT] ALT TEXT: "[description]"      │
├────────────────────────────────────────────┤
│ REFERENCE: Troubleshooting table           │
│ Error | Cause | Fix | Accessibility Note          │
├────────────────────────────────────────────┤
│ FOOTER: Owner • Version (large print avail) │
│ Screen reader tip • Keyboard shortcut noted  │
└────────────────────────────────────────────┘

UDL REQUIREMENTS:
☐ Information in ≥2 formats (text + visual min)
☐ All visuals have meaningful alt text
☐ Plain language option available
☐ Print-friendly (high contrast B/W works)
☐ Mobile-responsive layout
☐ Reading level: [X] grade or lower
☐ Jargon defined inline or linked glossary
☐ Color: Use BCBSKS palette (Blue/Midnight/Sky)
☐ Contrast: 4.5:1+ ratio minimum
☐ Fonts: Georgia Bold/Georgia
☐ Licensee disclosure if applicable
```

### Template E: Video Script (Accessible Multimedia)

```
Act as Multimedia Scriptwriter specializing in accessible educational video production.

Create AV script for [DURATION] video on [TOPIC].

THREE-COLUMN ACCESSIBLE SCRIPT:
┌──────────┬──────────────────┬──────────────────────┐
│ TIMECODE │ VISUAL           │ AUDIO                │
│          │                  │                      │
│          │ AD NOTES:        │ CAPTION TEXT:        │
│          │ [Audio desc for  │ [Exact caption copy]  │
│          │  blind viewers]  │                      │
├──────────┼──────────────────┼──────────────────────┤
│ 0:00-0:30│ HOOK             │ [Spoken intro]       │
│          │ AD: Title card   │ CC: "Welcome to..."  │
└──────────┴──────────┴──────────┴──────────────────────┘

PRODUCTION RULES:
• Every visual change gets AD note
• On-screen text read aloud OR described
• Color-coded elements also labeled text/icons
• Animations never convey meaning alone
• Spoken content duplicated in Captions exactly
• Sound effects noted: [SFX: chime]
• Speaker ID: [NARRATOR:] [SME:]
• Pronunciation: [(pro-NUN-cee-AY-shun)]
• Pace: max 140 words/min spoken
• Define terms first use
• Include BCBSKS terminology naturally

POST-PRODUCTION DELIVERABLES:
☐ Final video (MP4) ☐ Caption file (.SRT verbatim)
☐ Audio description track ☐ Transcript PDF (accessible)
☐ Thumbnail with alt text ☐ Chapter markers
```

### Template F: Facilitator Guide (Inclusive Delivery)

```
Act as Training Program Manager specializing in accessible facilitation for healthcare training.

Create session agenda/guide for [TRAINING TOPIC].

PER SEGMENT INCLUDE:
• Timing (start/end + processing buffer)
• Learning objective addressed
• Activity type WITH MODIFICATIONS:
  - Standard method
  - Alt for visual impairment
  - Alt for hearing impairment
  - Alt for mobility difference
  - Alt for cognitive/neurodifference
• Key talking points
• Transition phrase

FACILITATOR ACCESSIBILITY TOOLKIT:

□ PRE-SESSION:
  ☐ Send materials 48+ hours ahead
  ☐ Confirm room accessibility
  ☐ Test all tech (mic, captions, screen share)
  ☐ Prepare digital handouts (accessible PDF)
  ☐ Identify quiet space for sensory breaks

□ DURING SESSION:
  ☐ Describe all visuals aloud
  • Repeat questions before answering
  ☐ Face room when speaking (lip-reading)
  ☐ Use chat for key terms + verbal confirm
  ☐ Offer multiple participation modes
  ☐ Movement/stretch break every 25-30 min
  ☐ Signal topic transitions clearly
  ☐ Summarize key points at segment end

□ MATERIALS CHECKLIST:
  ☐ Slides with alt text ready
  ☐ Transcript/caption loaded
  ☐ Handouts large print (18pt+) available
  ☐ Digital version screen-reader tested
  ☐ Glossary distributed
  ☐ Recording consent obtained per BCBSKS policy
```

### Template G: Follow-Up Email Sequence (Inclusive Reinforcement)

```
Act as Learning Reinforcement Specialist with focus on multi-modal spaced practice.

Create follow-up sequence for [TOPIC] delivered to [AUDIENCE: members / providers].

EMAIL SEQUENCE:
┌──────┬────────────┬──────────┬──────────────────────┐
│ Day  │ Purpose    │ Tone     │ UDL Format Options   │
├──────┼────────────┼──────────┼──────────────────────┤
│ 0    │ Thank +    │ Warm     │ Text email + video   │
│      │ resources  │          │ summary + audio recap│
├──────┼────────────┼──────────┼──────────────────────┤
│ 3    │ Knowledge  │ Curious  │ Quiz (written OR oral │
│      │ check      │          │ OR visual matching  │
├──────┼────────────┼──────────┼──────────────────────┤
│ 7    │ Application│ Encourage│ Task card (text) +  │
│      │ challenge  │          │ demo video + checklist│
├──────┼────────────┼──────────┼──────────────────────┤
│ 14   │ Deeper dive │ Insightful│ Article (readable)  │
│      │            │          │ + podcast episode    │
└──────┴────────────┴──────────┴──────────────────────┘

PER EMAIL UDL:
☐ Subject: [Clear, descriptive]
☐ Body: max 150 words. Short paragraphs.
☐ ONE clear CTA
☐ Links: descriptive: [LINK: "Read article on X"]
☐ Plain text version available
☐ Colors: Use BCBSKS palette (Blue/Midnight/Sky)
☐ Images: alt text or marked decorative
☐ RECOMMENDED: Send via [BCBSKS email system if applicable
```

### Template H: Project Timeline / Gantt (Inclusive Production)

```
Act as Training Project Manager with expertise in accessible production workflows.

Create project timeline for [PROJECT NAME].

TIMELINE WITH ACCESSIBILITY MILESTONES:
┌─────────┬────────────┬──────┬───────┬─────────┬────────┬────────┐
│ Phase   │ Task       │Owner │Start  │End    │A11y Gate│
├─────────┼────────────┼──────┼───────┼─────────┼────────┼────────┤
│ANALYSIS │ Needs assess│ID    │Wk1    │Wk1    │☐ Learner│
│         │ incl. a11y  │      │        │        │  profile│
│         │ audit      │      │        │        │  captured│
├─────────┼────────────┼──────┼───────┼─────────┼────────┼────────┤
│DESIGN   │ Outline w/  │ID    │Wk2    │Wk3    │☐ UDL   │
│         │ UDL map    │      │        │        │  matrix │
│         │ completed│      │        │        │  filled │
├─────────┼────────────┼──────┼───────┼─────────┼────────┼────────┤
│DEVELOP  │ Slide deck  │ID    │Wk5    │Wk7    │☐ Alt txt│
│         │ created  │      │        │        │  written│
│         │            │      │        │        │  ☐Contrast│
├─────────┼────────────┼──────┼───────┼─────────┼────────┼────────┤
│REVIEW  │ SME review│ID+   │Wk7    │Wk8    │☐ A11y   │
│         │ + a11y audit│SME  │        │        │  passed │
├─────────┴─────────┴────────┴────────┴────────┴────────┴────────┴────────┤
│LAUNCH  │ Delivery  │All   │Wk12   │Wk12   │☐ Accom- │
│         │            │      │        │  modations│
└─────────┴─────────┴────────┴────────┴────────┴────────┴────────┘

GATE DEFINITIONS:

GATE 1 — Learner Profile Audit:
□ Disability representation in personas
□ Technology/access constraints documented
□ Accommodation requests anticipated

GATE 2 — UDL Matrix Complete:
□ Each LO mapped to ≥1 engagement option
□ Each content piece mapped to ≥2 rep formats
□ Each assessment mapped to ≥2 expression methods

GATE 3 — Asset Accessibility Review:
□ All images: meaningful alt text
□ Colors: contrast meets WCAG AA (4.5:1+)
□ Documents: screen-reader testable
□ Videos: captions + transcript
□ Interactive: keyboard-navigable
□ Time limits: extension mechanism exists

GATE 4 — Pre-Launch Verification:
□ Accommodation versions prepared
□ Facilitators briefed on inclusive delivery
□ Feedback mechanism includes a11y rating
□ Post-launch remediation plan documented
□ Licensee disclosure included where required
```

---

## §4.5 ⭐ Quick-Start One-Liners

**Copy-paste optimized prompts for daily tasks. Embed quality standards and UDL defaults.**

| Task | Optimized One-Line Prompt |
|------|---------------------------|
| **Summarize a document** | `"Summarize [attached doc] into [N] key points for [audience]. Bulleted list. Reading level: [X] grade. Glossary for jargon. Highlight actionable vs informational."` |
| **Generate quiz questions** | `"Write [N] [MCQ/scenario/open-ended] questions at Bloom's [level] testing [topic/skill]. Answer key with rationale. 2 formats: scenario-based and direct."` |
| **Simplify complex content** | `"Rewrite [content] at [X] grade reading level preserving accuracy. Analogy per concept. Flag meaning loss with [???]."` |
| **Create a rubric** | `"Design rubric with [N] criteria and [N] levels (1-[N]) for assessing [skill/output]. Descriptive anchors. Learner-friendly."` |
| **Convert format** | `"Transform [source format] into [target format]. Maintain [key elements]. Add [accessibility feature]."` |
| **Write an email** | `"Draft [purpose] email about [topic] for [audience]. Subject specific. Body under 150 words. One CTA. Plain text friendly. Links descriptive."` |
| **Create talking points** | `"Generate [N] talking points about [topic] for [role/context]. 1-2 sentences max each. Data point/example per point. Must-say vs optional."` |
| **Build an FAQ** | `"Create FAQ covering [topic] for [audience]. [N] questions. Answers: concise (2-3 sentences), actionable, jargon-free. Organized by category."` |
| **Design icebreaker` | `"Create [duration]-min icebreaker for [training topic] that [engages/reveals knowledge/builds]. Inclusive (no physical requirement). Low-stakes. Include script."` |
| **Write feedback** | `"Draft constructive feedback on [work product] for [recipient]. Focus on: (1) what's working well (specific), (2) 1-2 priority improvements (examples), (3 encouraging close."` |
| **Create glossary** | `"Extract technical/jargon from [content]. Glossary: definition plain language, example usage, related terms. Alphabetical. Reading level: [X] grade."` |
| **Generate discussion prompts** | `"Write [N] discussion prompts for [topic]. Open-ended, connect to real experience, avoid yes/no. Include probes."` |
| **Outline presentation** | `"Create [duration]-min outline on [topic] for [audience]. [N] sections. Per section: title, key message (1 sentence), supporting points (2-3 bullets), suggested visual, engagement moment."` |
| **Review & critique** | `"Act as critical SME reviewer. Review [content] for: (1) factual accuracy gaps, (2) instructional weaknesses, (3) accessibility oversights, (4) clarity issues. Flag with [REVIEW:] tags."` |
| **Fix problematic output** | `"Revise [content] to address: [specific problem]. Preserve what works. Fix only what was flagged. Mark unresolvable with [???]."` |
| **Create checklist** | `"Build step-by-step checklist for [task/process]. Numbered. Action verbs start each item. Prerequisites, common mistakes, completion criteria, escalation trigger."` |
| **Write learning objectives** | `"Write [N] measurable LOs for [topic/program] at Bloom's [level(s)]. Format: 'Given [condition], learners will [action verb] [performance criteria].' Observable and assessable."` |
| **Generate scenarios** | `"Create [N] realistic workplace scenarios involving [topic/skill] for [audience]. Context setup, dilemma, 3 options (one optimal), consequence, debrief takeaway."` |
| **Plan training agenda** | `"Design [duration] session agenda for [training topic]. Timing per segment, activity types, LO per segment, material needed, facilitator cue. Breaks every 25 min."` |

---

## §4.6 ⚠️ AI Limitations & Human Review Gates

**Critical: AI Cannot Replace Human Judgment**

| AI Output Type | ⚠️ What AI Cannot Reliably Do | ✅ Human MUST Verify |
|---------------|-------------------------------|---------------------|
| **Technical procedures** | Know if steps match current software/version | Test against live system or SME walkthrough |
| **Compliance/legal** | Know current regulations/laws; guarantee compliance claims | Legal/compliance authority review |
| **Cultural/social** | Avoid stereotypes; represent cultures authentically | Diverse reviewer panel |
| **Assessment validity** | Know if question measures stated objective | SME validation + pilot test |
| **Accessibility claims** | Actually test with assistive technology | Real AT testing (NVDA/JAWS/VoiceOver) |
| **Tone calibration** | Match BCBSKS unique voice perfectly | Stakeholder sample review |
| **Factual accuracy** | Not hallucinate citations/statistics/dates | Source verification against authoritative source |
| **Image descriptions** | Know what's visually important for blind/low-vision users | Blind/low-vision user review |

---

## §4.7 🔗 Prompt Chaining Workflow

**For multi-asset programs. The Review & Critique step is non-negotiable.**

### Standard Chain:

**STEP 1: ANALYSIS** → Analyze sources → Objectives matrix
**STEP 2: OUTLINE** → Storyboard with UDL columns
**STEP 3: DRAFT** → Apply matching Template (A-H) per asset
**STEP 4: REVIEW** ⭐ → Critical SME+a11y review (flag [FACT-CHECK:], [WEAKNESS:], [A11Y-GAP:], [CLARITY:])
**STEP 5: REVISE** → Address flags; preserve unflagged content; mark [???] if unresolved
**STEP 6: **FINAL QA** → Run §11 checklist (human step)

---

## §5 Complete Training Asset Library (33 assets + UDL)

### Category 1: Learning Materials (9 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Slide Deck** | ID | Core visual content presenting topics | Live, VILT, LMS | ❤️🧠✅ Alt text all images; 24pt+ font; high contrast; describe visuals verbally; speaker notes as transcript; downloadable text version |
| **Participant Guide** | ID | Detailed reference mirroring slides + exercises | PDF, Print, LMS | 🧠✅ Tagged PDF; searchable; 12pt+ body; structured headings; large-print version; dyslexia-friendly font option |
| **Facilitator Guide** | ID/SME | Step-by-step instructions: timing, prompts, answers, tips | PDF, Print | ❤️✅ Modification notes for different abilities; scripts for describing activities; cue cards; pacing adjustments |
| **Virtual Training Scripts** | ID/Trainer | Scripted virtual delivery: cues, polls, breakout instructions | PDF, Word | ❤️🧠✅ Captioning cues; chat-backup; screen-share a11y checks; multiple participation pathways |
| **Videos/Demonstrations** | ID/Multimedia | Short clips showing procedures, examples | MP4, LMS | 🧠✅ Sync captions (99%+); audio description track; transcript; no flashing; player controls accessible |
| **Audio Clips/Voiceovers** | ID/Audio Specialist | Narration or supplemental audio | MP3, Embedded | 🧠 Full transcript; adjustable playback; visual sync; no audio-only critical info |
| **Infographics/Charts/Diagrams** | ID/Graphic Designer | Visual representation of key points, processes | PNG, PDF, Slide | 🧠 Detailed alt text; data table alternative; colorblind-safe palette; scalable vector; text labels on data |
| **Screenshots/Step Guides** | ID/SME | Step-by-step visual instructions | PDF, Embedded | 🧠✅ Numbered callouts; text alt per step; zoomable; keyboard shortcuts noted |
| **Interactive Media/Simulations** | ID/Multimedia | Hands-on exercises in controlled environment | LMS, Web | ❤️🧠✅ Keyboard operable; screen reader compatible; no time pressure; error tolerance; hint system; skip/retry |

### Category 2: Interactive Assets (5 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Polls/Quizzes** | ID/Trainer | Short assessments embedded during session | LMS, Live | ❤️🧠✅ Verbal+visual poll display; extra response time; anonymous option; multiple response types |
| **Scenarios/Case Studies** | ID/SME | Realistic examples to analyze or solve | PDF, LMS, Live | ❤️🧠✅ Diverse characters; multiple solution paths; no ability-dependent advantage; scaffolded hints |
| **Role-Play Guides** | ID/Trainer | Instructions for practicing interpersonal skills | PDF | ❤️✅ Written alt to oral; observation option; script support; clear success criteria |
| **Hands-On Exercises** | ID/Trainer/SME | Task-based exercises for skill application | PDF, LMS, Live | ❤️✅ Multiple completion methods; AT compat checked; worked example first; graduated complexity; extended time |
| **Gamification/Challenges** | ID/Multimedia | Game-like activities to motivate/reinforce | LMS, Live | ❤️🧠✅ Not speed-dependent; multiple achievement paths; sound optional; color-independent mechanics |

### Category 3: Assessments & Evaluation (4 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Pre-Training Assessment** | ID | Baseline knowledge check to identify gaps | LMS, Paper | ❤️🧠✅ Low-stakes framing; varied formats; extra time; read-aloud option; results supportive |
| **Post-Training Assessment** | ID | Measures knowledge gained after instruction | LMS, Paper | ❤️🧠✅ Multiple modalities (choose format); open-book where appropriate; retake opportunity; rubric shared |
| **Practical/Skills Assessment** | ID/Trainer/SME | Demonstration of applied skills to verify competency | Observation, LMS | ❤️✅ Criteria shared advance; demonstration OR verbal explanation accepted; broken sub-tasks; practice attempt before graded |
| **Evaluation/Feedback Forms** | ID | Learner feedback on content, delivery, effectiveness | LMS, Paper | ❤️🧠✅ Multiple response formats; accessible form design; anonymous option; ask about accessibility specifically |

### Category 4: Digital/LMS Assets (4 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **E-Learning Module** | ID/Multimedia | Interactive self-paced training including media, quizzes, exercises | SCORM, LMS | ❤️🧠✅ WCAG compliant; keyboard nav; screen reader tested; adjustable pace; bookmarking; transcript; glossary pop-up; search |
| **SCORM/xAPI Files** | ID/LMS Specialist | Format for tracking learner progress within LMS | SCORM, xAPI | ✅ Completion criteria flexible; progress visible; accommodates varied pacing |
| **Resource Links/PDFs** | ID | Supplemental readings or references | LMS, PDF | 🧠 Tagged/accessible PDFs; diverse format options; reading level noted; external links a11y-tested |
| **Discussion Board/Forum Prompts** | ID/Trainer | Prompts for asynchronous learner engagement | LMS, Teams | ❤️🧠✅ Text AND video/audio response options; threaded view accessible; moderation guidelines; async-friendly |

### Category 5: Administrative/Support Materials (4 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Session Agenda/Schedule** | ID/Trainer | Sequence and timing of topics, exercises, breaks | PDF, Print | ❤️🧠 Break times prominent; sensory break reminders; multi-format agenda; 48hr+ advance distribution |
| **Attendance/Tracking Sheets** | ID/Trainer | Verification of participation for live/virtual sessions | Paper, LMS | ✅ Digital option; self-report alternative; private display; flexible definitions |
| **Certificates/Badges** | ID/LMS Specialist | Recognition of completion or achievement | PDF, LMS | 🧠 Screen-readable cert; alt format available; transparent criteria; licensee disclosure included |
| **Technical Setup Guide** | ID/IT Support | Instructions for trainers/participants on platforms/software | PDF, Email | 🧠✅ Screenshots+text; a11y features how-to; tech support contact; browser/device compatibility |

### Category 6: Supplemental & Reinforcement Materials (4 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Follow-Up Emails/Reminders** | ID/Trainer | Reinforce learning and provide post-session resources | Email, LMS | ❤️🧠 Plain text version; scannable; multiple resource formats; subject lines clear; unsubscribe easy |
| **Cheat Sheets/Job Aids** | ID | Quick reference guides for tools or processes | PDF, LMS, Print | 🧠✅ See Template D spec; large print; pocket-card; digital searchable; icon+text labels |
| **Infographic Summaries** | ID/Graphic | Visual recap of key points for retention | PDF, PNG, LMS | 🧠 Long-form text alt; data table for charts; colorblind-safe; logical reading order; SVG |
| **CoP Discussion Guides** | ID/Trainer | Ongoing peer learning and application guidance | LMS, Teams | ❤️🧠✅ Async-first; multiple contribution modes; inclusive guidelines; recording+transcript |

### Category 7: Planning & Tracking Tools (3 assets)

| Asset | Owner | Description | Delivery | UDL Considerations |
|-------|-------|-------------|----------|--------------------|
| **Gantt-Timeline** | ID | Maps asset creation, review, delivery, post-training lifecycle | Project tool, Spreadsheet | ✅ See Template H gates; a11y milestones explicit; buffer for remediation; diverse team feasibility |
| **Traffic-Light/Dashboard** | ID | Color-coded visual tracking of asset completion | Spreadsheet, Dashboard | 🧠 Status not color-alone (add text labels); screen reader table; filterable views; accessible chart alts |
| **Version Control/Repository** | ID | Central location for all assets to track iterations | SharePoint, Drive, Git | 🧠✅ Consistent naming (a11y version noted); structured folders; accessible files prioritized; metadata includes a11y status |

---

## §6 ♿ UDL Deep Dive

### The Three UDL Principles

#### ❤️ Engagement (The WHY) — Stimulating Interest & Motivation

- **7.1** Optimize choice & autonomy
- **7.2** Optimize relevance, value, authenticity
- **7.3** Minimize threats & distractions
- **8.1** Heighten salience of goals & objectives
- **8.2** Vary demands & resources
- **8.3** Foster collaboration & community
- **9.** Promote expectations & beliefs
- **9. ** Facilitate coping skills & strategies
- **9. ** Develop self-assessment & reflection

**Prompt Magic Words:** "choice," "relevance hook," "self-check," "opt-out," "low-stakes," "collaborative," "reflection prompt," "vary challenge"

#### 🧠 Representation (The WHAT) — Presenting Information & Content

- **1.1** Offer customs of displaying information
- **1.2** Offer alternatives for auditory information
- **1.#### **1.3** Offer alternatives for visual information
- **2.1** Clarify vocabulary & symbols
- **2.2** Clarify syntax & structure
- **2.3** Support decoding of text/math notation
- **3.** Activate/background knowledge
- **3.** Highlight patterns, critical features
- **3. ** Guide information processing

**Prompt Magic Words:** "multi-format," "alt text," "caption," "transcript," "glossary," "analogy," "visual organizer," "chunked," "plain language"

#### ✋ Action & Expression (The HOW) — Demonstrating Knowledge & Skills

- **4.1** Vary physical actions for response
- **4.2** Optimize access tools & AT
- **5.** Compose in multiple media
- **5.** Use multiple construction tools
- **5.** Build fluencies with graduated levels of support
- **6.** Guide goal-setting
- **6.** Support planning & strategy development
- **6. ** Manage information & resources
- **6.** Enhance capacity for monitoring

**Prompt Magic Words:** "multiple modalities," "keyboard accessible," "scaffolded," "worked example," "choice of output," "template provided," "rubric shared," "flexible deadline"

### UDL × Bloom's Alignment Matrix

| Bloom's | UDL Engagement | UDL Representation | UDL/Expression |
|---------|---------------|-------------------|----------------|
| **Remember** | Recall via quiz/flashcards/matching | Vocab in text+audio+visual glossary | Type, speak, draw, select |
| **Understand** | Connect to personal context; student-chosen analogy | Explain ± jargon + metaphor library | Summarize orally, write, concept-map |
| **Apply** | Real-world scenario of learner's choice | Worked example + blank template + video | Practice in sandbox, with peer, solo |
| **Analyze** | Analyze case relevant to learner's role | Data in table+chart+narrative; highlight patterns | Written analysis, oral, annotated diagram |
| **Evaluate** | Self-assessment against personalized criteria | Rubric in text+checklist+exemplar comparison | Peer review, self-rating, portfolio defense |
| **Create** | Open-ended project with topic choice | Resource bank multi-format; template options | Build, write, record, design, code — learner's choice |

---

## §7 🎨 BCBSKS Style Bible (Brand Kit Integrated)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BLUE CROSS AND BLUE SHIELD OF KANSAS (BCBSKS) ID STYLE GUIDE (UDL-INTEGRATED)
Non-negotiable rules for ALL training asset outputs:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━↓↓↓
```

---

## §8 Training Lifecycle Mapping (with UDH Touchpoints)

| Stage | Focus | Assets Active | UDH Touchpoints |
|-------|-------|------------|---------------|
| **Pre-Training** | Slides, Participant Guide, Facilitator Guide, Videos, Pre-Assessments, Tech Setup Guide | 🧠 Alt text • ✅ Keyboard tested • ❤️ Low-stakes pre-assessment • Materials sent 48hr+ • Large print ready • Captions finalized |
| **Live Training** | Slides, Facilitator Guide, Scenarios, Exercises, Role-Plays, Polls, Attendance | ❤️ Describe visuals aloud • Repeat questions • Multiple participation modes • Movement breaks • Lighting/seating checked |
| **Virtual Training** | Virtual Scripts, Slides, Polls, Breakouts, Previews | 🧠 Live captions • Chat backup • Screen share accessible • Recording for async • Camera-optional |
| **Post-Training** | Post-Tests, Feedback Forms, Follow-Up Emails, Cheat Sheets, Infographics, Certificates | ❤️ Modality choice • 🧠 Multi-format resources • Certificates accessible • Retakes available |
| **LMS / Self-Paced** | E-Learning Modules, SCORM/xAPI, Resources, Discussions, Downloadables | ✅ Full WCAG audit • Media captioned+transcribed • Adjustable pace • Bookmarking • Progress visible |
| **Ongoing Support** | CoP Guides, Refreshers, Updated Job Aids, Gamification | ❤️ Async-first CoP • Updated materials inherit UDL • Meetings transcribed • New job aids UDL-default |

---

## §9 Best Practices (+ BCBSKS Standards)

1. **Align assets with learning objectives** — Map each objective to UDL options
2. **Develop high-impact assets first** — Ensure born-accessible
3. **Design modular assets for reuse** — Make accessibility part of module
4. **Plan for multiple delivery modes** — Live, virtual, LMS. Each has unique a11y requirements
5. **Include post-training reinforcement** — Emails, CoP discussions, job aids, spaced practice
6. **Build in review cycles** — Include accessibility in every cycle
7. **Track progress visually** — Include a11y milestones in dashboards/Gantt
8. **Allow realistic timelines** — Add 15-20% buffer for a11y remediation
9. **Incorporate feedback loops** — Specifically ask about accessibility experience
10. **Ensure accessibility & compliance** — Alt text, captions, readable fonts, WCAG
11. **⭐ Design for variability from Day 1** — Don't **Retrofit.** Build UDL into prompts from start
12. **⭐ Offer choice wherever possible** — Choice IS the accommodation
13. **⭐ Assume nothing about learners** — Design for margins

### 🏢 Additional BCBSKS-Specific Standards

- [ ] **Compliance:** Ensure all materials meet BCBSKS Corporate Style Guide requirements
- [ ] **Logo Usage:** Use primary logo for most communications; secondary logo for limited-space applications
- [ ] **Colors:** Use core palette (Blue, Midnight, Bluejay, Sky, grays). Extended palette (Bellflower, Buffalo, Cottonwood, Fiesta) for accents only
- [ ] **Fonts:** Georgia Bold/Georgia for headings; Arial/Georgia for body text
- [ ] **Tone:** Conversational, warm, human-first, community-centered (Plain Talk standard)
- [ ] **Writing Style:** 
  - Use "Blue Cross and Blue Shield of Kansas" (full name) at first mention
  - Acceptable alternatives: BCBSKS, Blue Cross, the Kansas company, our company
  - Avoid: BCBSSKS, BlueCrossBlueShield of Kansas, Kansas Blue Cross and Blue Shield's
  - **Always write "Blue Cross and Blue Shield"** — never "Cross and Shield" alone
- [ ] **Legal/Compliance:**
  - Include licensee disclosure where required
  - Follow BCBSKS Corporate Style Guide for capitalization, punctuation, and formatting
  - Use full legal entity name for external materials
- [ ] **Accessibility:**
  - WCAG 2.** **AA** compliance for all digital assets
  - Screen reader compatibility for all documents
  - Captions for all video/audio
  - Alt text for all images
  - Keyboard navigation for interactive content
  - Time limits with extension mechanism
- [ ] **Review & Approval:**
  - External/public comms: externalcomms@bcbks.com
  - Internal questions: corpcomm@bcbks.com
  - Logo/graphics: bcreative@bcbks.com
  - Legal: legal.services@bcbks.com
- [ ] **Distribution:**
  - Approved channels: [your org's approved channels]
  - Version control: [your org's system]
  - Retention schedule: [your org's retention schedule]

---

## §10 Quick Reference Cards + ❌ Anti-Patterns

### Bloom's + UDL Verb Matrix

| Level | Verbs | UDL Engagement | UDL Representation | UDL/Expression |
|-------|-------|---------------|-------------------|-------------------|
| **1-2: Remember&Understand** | Recall via quiz/flashcards/matching | Explain ± jargon + metaphor library | Type, speak, draw, select |
| **3-4: Apply&Analyze** | Apply via sandbox/role-play/written | Worked example + blank template + video demo | Practice in sandbox, with peer, solo |
| **5-6: Evaluate&Create** | Evaluate via rubric/self-peer-review | Create via project/video/portfolio — learner's choice |

### UDL "Always Include" Checklist

**❤️ Engagement:** ☐ Relevance hook ☐ Choice option ☐ Self-check ☐ Low-stakes signal ☐ Real-world connection ☐ Varied challenge level

**🧠 Representation:** ☐ ≥2 formats ☐ Jargon defined (inline + glossary) ☐ Alt text for visuals ☐ Captions/transcript for media ☐ Plain language summary

**✋ Action/Expression:** ☐ ≥2 demonstration methods ☐ Worked example first ☐ Scaffolded support ☐ Flexible timing ☐ Rubric shared upfront

**♿ Accessibility:** ☐ WCAG AA verified ☐ Keyboard nav ☐ Contrast ≥4. ### :** ☐ Screen reader tested ☐ No time limits without extension ☐ No flashing/flickering ☐ Form inputs labeled

### ❌ Anti-Patterns

| ❌ Anti-Pattern | 🔄 What Happens | ✅ Instead (Prompt Fix) |
|---------------|-----------------|-------------------|
| **"Just make it engaging"** | Adds gamification, emojis, stories — misses the point | `"Specify engagement type: relevance hook, choice of scenario context, self-reflection at [point]"` |
| **"Make it accessible" (after writing)** | AI slaps alt text as afterthought | `"Build accessibility into initial prompt (R-C-A-O-UO). Alt text, captions, reading level from start"` |
| **"Write at a professional level"** | Academic language; excludes many learners | `"Target [X] grade max. Define jargon inline. Provide plain-language summary option."` |
| **"Create a comprehensive guide"** | 40-page document nobody reads | `"One page. 300 words max. Job aid format. Modular if more needed."` |
| **"Generate realistic scenarios"** | Stereotypes, narrow contexts | `"Diverse representation in roles/names/settings. No ability-dependent plot points. Include disabled characters normatively."` |
| **"Assess their understanding"** | Single MCQ measures recall only | `"Offer 3 modalities: written analysis, oral explanation, practical demonstration. Let learner choose."` |
| **"Fix this" (no context)** | AI guesses wrong thing | `"The issue is [specific problem]. Don't **[wrong thing]**. Address only: [correct thing]." ``
| **Copying old prompts** | Wrong audience, tone, constraints carried over | `"Adapt R-C-A-O-U for THIS project: new audience, new stakes, new a11y requirements."` |

### Emergency Fixes (UDL-Aware)

| ❌ Problem | ✅ Fix Prompt |
|-----------|-------------|
| Too Generic | `"Go deeper. Add: (1) real example, (2) common mistake, (3) mnemonic, (4) visual organizer"` |
| Too Long | `"Cut 40%. Chunk into 5-min segments. Add progress indicators."` |
| Wrong Tone | `"Rewrite in [tone]. Match sample: [paste sample]. Keep inclusive language."` |
| Missing Visual Directions | `"Add [VISUAL:] + [ALT:] per item. Ensure color-independent."` |
| Not Accessible | `"Add alt text, captions, keyboard nav, reading level check, contrast audit."` |
| Single Modality Only | `"Add alternative: [audio/video/demo/hands-on/visual summary]"` |

---

## §11 ✅ Pre-Publish QA Checklist

### 📝 CONTENT ACCURACY (Quick: ~1min | Standard: ~2min)
- [ ] Facts verified against source material
- [ ] Procedures tested against live system (or flagged for SME)
- [ ] No hallucinated features/statistics/citations
- [ ] Citations/references accurate and current
- [ ] Proper nouns spelled correctly
- [ ] Dates and version numbers correct

### 🎓 INSTRUCTIONAL QUALITY (Quick: ~1min | Standard: ~2min)
- [ ] Learning objectives clear and measurable
- [ ] All content maps to objectives (no orphan content)
- [ ] Cognitive load appropriate (chunked, not overwhelming)
- [ ] Assessment matches objective level (Bloom's aligned)
- [ ] Logical flow/sequence makes sense
- [ ] Transitions between topics are clear
- [ ] Prerequisites identified and communicated

### ❤️ UDL: ENGAGEMENT (Quick: ~30sec | Standard: ~1min)
- [ ] Relevance hook included (why care?)
- [ ] Choice option offered somewhere
- [ ] Self-assessment/reflection moment included
- [ ] Low-stakes environment signaled
- [ ] Real-world connection explicitly stated
- [ ] Varied challenge level available

### 🧠 UDL: REPRESENTATION (Standard: ~1min | Full: ~2min)
- [ ] Content in ≥2 formats (minimum: text + visual)
- [ ] All jargon defined (inline + glossary)
- [ ] All meaningful images have alt text
- [ ] All video/audio has captions planned + transcript
- [ ] Plain language summary option available
- [ ] Reading level verified at or below target
- [ ] Color never used as sole information carrier

### ✋ ACTION/EXPRESSION (Quick: ~30sec | Standard: ~1min)
- [ ] Learners can demonstrate knowledge in ≥2 ways
- [ ] Worked example provided before independent practice
- [ ] Scaffolded support available (hints, templates, partial completion)
- [ ] Flexible timing/deadlines options noted
- [ ] Rubric or success criteria shared with learner upfront
- [ ] Assistive technology compatibility considered

### ♿ ACCESSIBILITY TECHNICAL (Standard: ~2-3min | Full: ~5min)
- [ ] WCAG AA compliance verified (contrast, focus, structure)
- [ ] Keyboard navigation confirmed (no mouse-required interactions)
- [ ] Color contrast ratio ≥4.5:1 (body), ≥3:1 (large text)
- [ ] Screen reader tested (or scheduled for testing)
- [ ] No time limits without clear extension mechanism
- [ ] No auto-playing audio/video without user control
- [ ] No flashing/flickering content (seizure risk)
- [ ] Form inputs properly labeled
- [ ] **[BCBSKS-Specific]** Licensee disclosure included where required
- [ ] **[BCBSKS-Specific]** Logo usage rules followed
- [ ] **[BCBSKS-Specific]** Color palette used correctly
- [ ] **[BCBSKS-Specific]** Typography (Georgia Bold/Georgia for headings, Arial/Georgia for body)
- [ ] **[BCBSKS-Specific]** Writing style (Plain Talk compliant)
- [ ] **[BCBSKS-Specific]** Logo usage (Primary vs Secondary vs Tertiary)
- [ ] **[BCBSKS-Specific]** Corporate writing style (capitalization, terminology)
- [ ] **[BCBSKS-Specific]** Prohibited words avoided (see §7)
- [ ] **[BCBSKS-Specific]** Date/number/date formatting
- [ ] **[BCBSKS-Specific]** Building/division naming conventions
- [ ] **[BCBSKS-Specific]** Approval workflow triggered (see §9)

### 🏢 [BCBSKS] ORGANIZATIONS

- [ ] **[BCBSKS-Specific]** Templates & channel specifications
- [ ] **[BCBSKS-Specific]** Starter patterns for common assets
- [ ] **[BCBSKS-Specific]** Review contacts for each gate
- [ ] **[BCBSKS-Specific]** Distribution channels
- [ ] **[BCBSKS-Specific]** File naming conventions
- [ ] **[BCBSKS-Specific]** Version control system

### 📦 DELIVERY READINESS (Quick: ~30sec | Standard: ~1min)
- [ ] **[BCBSKS-Specific]** Logo placement confirmed
- [ ] **[BCBSKS-Specific]** Licensee disclosure included
- [ ] **[BCBSKS-Specific]** Colors: Verified correct hex codes used
- [ ] **[BCBSKS-Specific]** Typography: Verified correct
- [ ] **[BCBSKS-Special]** Anti-patterns avoided (see §10)
- [ ] **[BCBSKS-Specific]** Compliance checkboxes completed

---

## 🚀️ The Professional ID's Mindset

This document gives you **four things**:

1. **A complete mental model** (R-C-A-O-U) for structuring any AI prompt
2. **A library of proven templates** (A-H) for every common training asset type
3. **Quality guardrails** (Anti-Patterns, AI Limitations, QA Checklist)
4. **A UDL default setting** — accessibility and inclusion built in, not bolted on

**The most important shift?** From *"How do I get AI to write this?"* → *"How do I prompt AI so output is accurate, accessible, effective, and ready for human verification?"*

---

*Version 4.0 — **Blue Cross and Blue Shield of Kansas (BCBSKS) Edition*
*Built on CAST UDL Guidelines 2.2 • WCAG 2. **AA** • Universal Design principles*
*Living reference — update Style Book as organizational standards evolve.*
*Customizable — see §0 for customization checklist.*



```
```

    
✚️
```
```


```
```
Blue Cross and Blue Shield of Kansas
```
```


```
```
        
```
```
© [Year] Blue Cross and Blue Shield of Kansas • Internal Use Document

```
```
    
```
```


```
```
        
```
```
Compatible with: ChatGPT • Claude • Gemini • Copilot • Perplexity • Not recommended for Perplexity

```
```
    



```
