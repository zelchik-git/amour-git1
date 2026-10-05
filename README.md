# 🎨 Concept Art Job Hunt Suite (Career-Ops & HH-Applicant-Tool Edition)

A local-first, privacy-focused job search and application automation platform built specifically for **Concept Artists & 2D Artists** targeting **Canada & Global Remote roles**.

Inspired by:
- **[Career-Ops](https://career-ops.org/)**: The open-source AI job search agent that uses **5-Dimension Rubric Scoring (1.0 to 5.0)**, the strict **4.0 Apply Line**, zero-token portal scanning, and automatic answers to open-ended **Greenhouse, Lever & Ashby** application questions.
- **[hh-applicant-tool](https://github.com/s3rgeym/hh-applicant-tool)**: The candidate automation utility featuring **spintax cover letter randomization** (to avoid duplicate spam filters), multi-profile management, local audit tracking logs, and anti-duplicate submission protection.

---

## 📂 Your Toolkit Files

| File | Description | How to Use |
|---|---|---|
| **[`index.html`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/index.html)** | **Full Visual Dashboard & Automation Cockpit** | Double-click to launch in Chrome, Edge, or Firefox. Zero install required. |
| **[`job_tracker_template.csv`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/job_tracker_template.csv)** | **Spreadsheet Import File** | Import into Google Sheets or download directly from the dashboard. |
| **[`google_apps_script.js`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/google_apps_script.js)** | **Google Sheets Automation Script** | Paste into Extensions > Apps Script in Google Sheets for dropdowns & auto-colors. |
| **[`ai_job_extractor_prompt.md`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/ai_job_extractor_prompt.md)** | **Universal AI Evaluator & /apply Prompt** | Copy into Gemini, ChatGPT, or Claude to parse any job link or text. |
| **[`boolean_job_search_prompts.md`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/boolean_job_search_prompts.md)** | **Search Queries & ATS X-Ray Strings** | Use on LinkedIn, Google, ArtStation, Greenhouse, and Lever. |
| **[`config.json`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/config.json)** | **Candidate Profile & Rubric Weights** | Customize your portfolio URL, skills, and ATS screening defaults. |
| **[`letter_template.txt`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/letter_template.txt)** | **Spintax Dynamic Cover Letter Template** | Phrasing variations with `{Option A\|Option B}` syntax. |
| **[`career_ops_art.py`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/career_ops_art.py)** | **Optional Python CLI Companion** | Run `python career_ops_art.py` for terminal-based scoring and drafting. |

---

## 🚀 Key Features Recreated & Upgraded in `index.html`

### 1. 🔍 Automated Vacancy Scanner & Role Parser (Career-Ops & HH-Applicant-Tool Hybrid)
- **Unified Vacancy Feed**: Aggregates and lists active concept art openings in one place from public ATS APIs (Greenhouse & Lever), remote design APIs (Remotive), and 25+ Canadian & Global Remote game studios.
- **Full Role Details on Every Vacancy**: Displays exact Job Title, Studio Name, Location & Work Arrangement (Hybrid/Remote), Salary range, Role Overview, Key Responsibilities, Hard Requirements, Software (Photoshop, Blender, ZBrush), and Date Posted.
- **1-Click "+ Add to Pipeline"**: Adds any vacancy directly into your Kanban Pipeline and Google Sheets table.
- **1-Click "🎯 5D Rubric & /apply"**: Instantly generates Greenhouse/Lever answers and calculates Career-Ops fit score.
- **Instant URL / Text Parser**: Paste any job link or raw description from LinkedIn, ArtStation, or Indeed to extract all role details automatically.

### 2. 🌟 Career-Ops 5-Dimension Evaluation Rubric & 4.0 Threshold
Instead of an arbitrary percentage, jobs are evaluated against a structured 5-dimension rubric (scored 1.0 to 5.0):
1. **Artistic Specialization & Style (Weight: 30%)**: Evaluates character/creature emphasis vs. props vs. environments.
2. **Software & 2D/3D Hybrid Pipeline (Weight: 25%)**: Photoshop, 3D blockout (Blender/ZBrush), turnarounds, and engine asset requirements.
3. **Seniority & Autonomy Scope (Weight: 15%)**: Fit against your Mid-level target.
4. **Location & Work Authorization (Weight: 20%)**: Full score for Canada (Montreal, Vancouver, Toronto) and Worldwide Remote contract.
5. **Studio Culture & Project Alignment (Weight: 10%)**: Game genre and art style synergy.
- **Global Score & Career-Ops Apply Threshold**:
  - `✅ STRONG GO (>= 4.0)`: High conviction match exceeding the apply threshold.
  - `⚠️ CONDITIONAL GO (3.5 - 3.9)`: Manual override required.
  - `❌ HARD PASS (< 3.5)`: Strategic skip to respect your artistic time.

### 2. 📝 Greenhouse, Lever & Ashby `/apply` Essay Assistant
Studio application forms constantly ask open-ended essay questions. The tool instantly drafts paste-ready answers:
- *"Why do you want to work at [Studio] on this project?"*
- *"Describe your concept art production workflow from initial thumbnail to final deliverable."*
- *"Link your portfolio and highlight your 2 most relevant pieces."*
- *"What is your work authorization status and availability?"*
- *"How do you handle creative feedback and art direction revisions?"*

### 3. 🎯 Role-Tailored CV Experience Bullets
Generates 3 ATS-optimized experience bullet points mapping your character concept art and 3D blockout skills directly to the keywords in the job description.

### 4. 🎲 Dynamic Spintax Cover Letter Studio (HH-Applicant-Tool Pattern)
Features nested spintax `{Option 1|Option 2|Option 3}` and provides 4 art templates:
- **Character & Creature Pitch**
- **3D Blockout & Props Specialist**
- **2D Visual Development Generalist**
- **Short Recruiter InMail Note**
Includes word counts, character counts, and a **"🎲 Re-roll Variation"** button generating over 25,000 unique phrasing permutations.

### 5. 🛡️ Anti-Duplicate Guard & Audit Trail
- **URL & Title Exact Match**: Flags duplicate links before you waste time applying.
- **Studio Blacklist Manager**: Automatically flags studios with unpaid tests or poor reviews.
- **Local Activity Audit Trail**: Timestamped history tracking all job additions, status updates, and exports.

### 6. ⚡ Studio & Search Hub (150+ Portals)
One-click search query launchers for:
- **ArtStation Jobs** (2D Concept Art)
- **LinkedIn** (Boolean Canada & Remote)
- **Greenhouse.io, Lever.co & AshbyHQ Google X-Ray Searches**
- **Work With Indies, Hitmarker, GamesJobsDirect**
- **Directory of 19+ Canadian & Global Remote Studios** (*Behaviour, Ubisoft Montreal/Toronto, The Coalition, EA, Digital Extremes, BioWare, Moon Studios, Riot, Bungie, etc.*)

### 7. ⏱️ Art Test Tracker & CAD/USD Day-Rate Calculator
- **Art Test Manager**: Log concept art tests, prompt briefs, submission deadlines, and compensation status.
- **Day-Rate & Salary Converter**: Convert hourly rates to day rates, monthly totals, and annual benchmarks in CAD and USD.

---

## 🏁 How to Start Right Now (Zero Coding)

1. Open this folder: `c:\Users\eshabalina\Downloads\lqa-prompts (1)\lqa-prompts\Stuff\`
2. Double-click **[`index.html`](file:///c:/Users/eshabalina/Downloads/lqa-prompts%20(1)/lqa-prompts/Stuff/index.html)**.
3. Click the **"5D Rubric & /apply"** tab, click **"Behaviour Interactive"** or **"Load Example"**, and watch the 5-dimension evaluation, `/apply` answers, and tailored CV bullets generate in real time!
4. Click **"Export CSV"** anytime to download your updated spreadsheet ready for Google Sheets.
