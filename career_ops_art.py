#!/usr/bin/env python3
"""
=============================================================================
🎨 CAREER-OPS (Concept Art Edition) & APPLICANT AUTOMATION TOOL
=============================================================================
Inspired by:
- career-ops (https://career-ops.org/) -> Local-first, 5-Dimension Rubric Scoring, ATS question generation.
- hh-applicant-tool (https://github.com/s3rgeym/hh-applicant-tool) -> Application logging, spintax cover letter randomization, anti-duplicate protection.

Run with:
    python career_ops_art.py
or:
    python career_ops_art.py score "job_description.txt"
    python career_ops_art.py apply "Studio Name" "Role Title"
    python career_ops_art.py scan
    python career_ops_art.py export
=============================================================================
"""

import sys
import os
import re
import json
import random
import csv
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
LETTER_PATH = os.path.join(os.path.dirname(__file__), "letter_template.txt")
CSV_PATH = os.path.join(os.path.dirname(__file__), "job_tracker_template.csv")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "candidate": {
            "name": "Concept Artist",
            "primary_specialization": "Character & Creature Concept Art",
            "seniority_level": "Mid-level",
            "location": "Canada",
            "portfolio_url": "https://www.artstation.com/your-portfolio"
        }
    }

def resolve_spintax(text):
    """
    Resolves {Option A|Option B|Option C} spintax blocks randomly
    to generate distinct, personalized application cover letters.
    """
    pattern = re.compile(r"\{([^{}]+)\}")
    while True:
        match = pattern.search(text)
        if not match:
            break
        options = match.group(1).split("|")
        chosen = random.choice(options)
        text = text[:match.start()] + chosen + text[match.end():]
    return text

def score_job_listing(job_text):
    """
    Career-Ops 5-Dimension Evaluation Rubric for Concept Artists:
    1. Artistic Specialization (Characters/Creatures vs Props vs Environments)
    2. Software & 2D/3D Pipeline (Photoshop, Blender, ZBrush, Turnarounds)
    3. Seniority & Scope Fit (Mid-level target)
    4. Location & Work Authorization (Canada / Worldwide Remote)
    5. Project Alignment & Studio Fit (Games, Film, Animation, TCG)
    """
    lower = job_text.lower()
    
    # Dimension 1: Specialization
    d1_score = 3.5
    d1_notes = []
    if any(k in lower for k in ["character", "creature", "costume", "anatomy", "faces", "humanoid"]):
        d1_score = 5.0
        d1_notes.append("High match: Direct Character & Creature concept focus.")
    elif any(k in lower for k in ["prop", "hard-surface", "weapon", "vehicle"]):
        d1_score = 4.2
        d1_notes.append("Good match: Prop / Hard-surface design alignment.")
    elif any(k in lower for k in ["environment", "landscape", "architecture"]):
        d1_score = 2.8
        d1_notes.append("Moderate match: Role centers primarily on Environment concept art.")
    elif any(k in lower for k in ["ui", "icon", "user interface"]):
        d1_score = 3.2
        d1_notes.append("Moderate match: 2D UI / Asset production focus.")

    # Dimension 2: Software & 2D/3D Pipeline
    d2_score = 4.0
    d2_notes = []
    if "photoshop" in lower or "2d" in lower:
        d2_notes.append("Photoshop 2D rendering pipeline verified.")
    if any(k in lower for k in ["3d", "blender", "zbrush", "maya", "blockout"]):
        d2_score = 5.0
        d2_notes.append("3D blockout (Blender/ZBrush to 2D paint-over) directly utilized.")
    if any(k in lower for k in ["unreal", "ue5", "unity"]):
        d2_score = min(d2_score, 4.0)
        d2_notes.append("Notice: Engine asset integration mentioned.")

    # Dimension 3: Seniority Fit
    d3_score = 5.0
    d3_notes = []
    if any(k in lower for k in ["senior", "sr.", "principal"]):
        d3_score = 3.2
        d3_notes.append("Caution: Position is Senior/Principal. Emphasize autonomy and strong portfolio.")
    elif any(k in lower for k in ["lead", "art director", "director"]):
        d3_score = 2.0
        d3_notes.append("Warning: Management/Lead scope.")
    elif any(k in lower for k in ["junior", "associate", "entry"]):
        d3_score = 4.5
        d3_notes.append("Favorable: Entry/Associate level, strong candidate advantage.")
    else:
        d3_notes.append("Ideal: Mid-level candidate target.")

    # Dimension 4: Location & Work Authorization
    d4_score = 3.0
    d4_notes = []
    if "canada" in lower or any(city in lower for city in ["montreal", "vancouver", "toronto", "quebec", "edmonton"]):
        d4_score = 5.0
        d4_notes.append("Authorized: Canada-based / Canadian studio hub.")
    elif any(rem in lower for rem in ["remote", "worldwide", "work from home", "anywhere", "global"]):
        d4_score = 4.8
        d4_notes.append("Eligible: Remote / Worldwide contract availability.")
    elif "united states" in lower or "us only" in lower:
        d4_score = 2.0
        d4_notes.append("Caution: US localized posting without explicit remote tag.")

    # Dimension 5: Project Alignment
    d5_score = 4.5
    d5_notes = ["Gaming / Entertainment industry production."]

    # Global Weighted Score (Career-Ops Rubric)
    # Weights: Specialization 30%, Pipeline 25%, Seniority 15%, Location 20%, Project 10%
    global_score = (
        (d1_score * 0.30) +
        (d2_score * 0.25) +
        (d3_score * 0.15) +
        (d4_score * 0.20) +
        (d5_score * 0.10)
    )
    pct = int((global_score / 5.0) * 100)

    verdict = "✅ STRONG GO" if global_score >= 4.0 else ("⚠️ CONDITIONAL GO" if global_score >= 3.2 else "❌ SKIP / MISMATCH")

    return {
        "global_score": round(global_score, 2),
        "percentage": pct,
        "verdict": verdict,
        "dimensions": {
            "1. Artistic Specialization": {"score": d1_score, "notes": d1_notes},
            "2. Pipeline & Tooling": {"score": d2_score, "notes": d2_notes},
            "3. Seniority & Scope": {"score": d3_score, "notes": d3_notes},
            "4. Location & Authorization": {"score": d4_score, "notes": d4_notes},
            "5. Project & Studio Alignment": {"score": d5_score, "notes": d5_notes}
        }
    }

def generate_ats_answers(studio_name, role_title, job_text, config):
    """
    Career-Ops `/apply` helper:
    Generates paste-ready answers for standard Greenhouse, Lever & Ashby open-ended questions.
    """
    cand = config.get("candidate", {})
    portfolio = cand.get("portfolio_url", "https://www.artstation.com/your-portfolio")

    q1 = f"Why do you want to work at {studio_name} as a {role_title}?"
    a1 = (
        f"I have closely followed {studio_name}'s artistic direction and creative vision. "
        f"As a Concept Artist specializing in character and creature design with strong prop fundamentals, "
        f"my goal is to contribute visually compelling, functional designs that reinforce your project's aesthetic. "
        f"I am eager to collaborate with your art team to iterate quickly on key production briefs and deliver assets that "
        f"energize both the development pipeline and the players."
    )

    q2 = "Describe your concept art workflow from initial brief to final delivery."
    a2 = (
        "My workflow begins with thorough visual research and rapid silhouette/thumbnail exploration to establish distinct "
        "readability and proportion. Once a visual direction is approved, I build basic 3D blockouts in Blender or ZBrush "
        "to nail perspective, lighting, and volume before bringing the asset into Photoshop for rendering, texture articulation, "
        "and material definition. I conclude with clean orthographic turnaround and callout sheets so 3D modelers have clear, "
        "production-ready blueprints."
    )

    q3 = "Link your portfolio and highlight which 2 pieces best demonstrate your fit."
    a3 = (
        f"Portfolio: {portfolio}\n\n"
        "Key highlights for this role:\n"
        "1. Character & Costume Design Series: Demonstrates anatomical proportion, costume functionality, and silhouette iteration across multiple variants.\n"
        "2. Creature / Prop Production Sheets: Illustrates 3D-to-2D paint-over workflow, material separation, and orthographic callouts for downstream production."
    )

    q4 = "What is your work authorization status and availability?"
    a4 = (
        "I am legally authorized to work in Canada without requiring visa sponsorship, and I am also fully equipped "
        "for worldwide remote / B2B contract collaboration with a dedicated professional workstation and high-speed fiber connection. "
        "Available to start within standard 2-week notice."
    )

    return [
        {"question": q1, "answer": a1},
        {"question": q2, "answer": a2},
        {"question": q3, "answer": a3},
        {"question": q4, "answer": a4}
    ]

def generate_cover_letter(studio_name, role_title, config):
    """
    Generates a personalized cover letter using the spintax template (hh-applicant-tool pattern).
    """
    cand = config.get("candidate", {})
    if os.path.exists(LETTER_PATH):
        with open(LETTER_PATH, "r", encoding="utf-8") as f:
            template = f.read()
    else:
        template = "Hi {company} team,\n\nApplying for {role}.\nPortfolio: {portfolio}\n\nBest,\n{name}"

    letter = resolve_spintax(template)
    letter = letter.replace("{company}", studio_name)
    letter = letter.replace("{role}", role_title)
    letter = letter.replace("{portfolio}", cand.get("portfolio_url", "https://www.artstation.com/your-portfolio"))
    letter = letter.replace("{name}", cand.get("name", "Concept Artist"))
    return letter

def print_banner():
    print("=" * 75)
    print("🎨 CAREER-OPS (Concept Art Edition) & APPLICANT AUTOMATION TOOL")
    print("   5-Dimension Rubric Scoring • ATS Form Assistant • Spintax Outreach")
    print("=" * 75)

def interactive_cli():
    config = load_config()
    print_banner()

    while True:
        print("\nMain Menu:")
        print("1. 📊 Score a Job Posting (Career-Ops 5-Dimension Rubric)")
        print("2. 📝 Generate ATS Application Answers (Greenhouse / Lever / Ashby)")
        print("3. ✉️ Generate Randomized Cover Letter (Spintax / HH-Applicant-Tool)")
        print("4. 🌐 View Quick Portals & Studio Directory (Canada & Remote)")
        print("5. 📥 View Tracked Jobs in CSV")
        print("6. 🚪 Exit")

        choice = input("\nSelect an option [1-6]: ").strip()

        if choice == "1":
            print("\nPaste the job description (Type 'END' on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            job_text = "\n".join(lines)
            if not job_text.strip():
                print("No text provided.")
                continue

            result = score_job_listing(job_text)
            print("\n" + "=" * 50)
            print(f"GLOBAL FIT SCORE: {result['global_score']} / 5.0 ({result['percentage']}%) -> {result['verdict']}")
            print("=" * 50)
            for dim, data in result["dimensions"].items():
                print(f"\n{dim}: [{data['score']} / 5.0]")
                for n in data["notes"]:
                    print(f"  • {n}")
            print("\n" + "=" * 50)

        elif choice == "2":
            studio = input("Enter Studio Name (e.g. Behaviour Interactive): ").strip() or "Game Studio"
            role = input("Enter Role Title (e.g. Character Concept Artist): ").strip() or "Concept Artist"
            answers = generate_ats_answers(studio, role, "", config)
            print("\n" + "=" * 60)
            print(f"🎯 DRAFTED ATS QUESTION ANSWERS FOR {studio.upper()}:")
            print("=" * 60)
            for item in answers:
                print(f"\n[Q]: {item['question']}")
                print(f"[A]:\n{item['answer']}\n")
            print("=" * 60)

        elif choice == "3":
            studio = input("Enter Studio Name (e.g. Ubisoft Montreal): ").strip() or "Game Studio"
            role = input("Enter Role Title (e.g. Mid-Level Concept Artist): ").strip() or "Concept Artist"
            letter = generate_cover_letter(studio, role, config)
            print("\n" + "=" * 60)
            print(f"✉️ PERSONALIZED COVER LETTER ({studio}):")
            print("=" * 60)
            print(letter)
            print("=" * 60)

        elif choice == "4":
            print("\nScanning live remote design & concept art vacancies...")
            try:
                import urllib.request
                req = urllib.request.Request(
                    "https://remotive.com/api/remote-jobs?category=design&limit=10",
                    headers={"User-Agent": "CareerOpsArt/1.0"}
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    jobs = data.get("jobs", [])
                    print(f"\nFound {len(jobs)} live vacancies from public ATS feeds:\n")
                    for i, j in enumerate(jobs[:8], 1):
                        print(f"[{i}] {j.get('title')} @ {j.get('company_name')}")
                        print(f"    Location: {j.get('candidate_required_location')} | URL: {j.get('url')}\n")
            except Exception as e:
                print(f"Live scan notice (offline/timeout): {e}")
                print("\nShowing Top Curated Canadian & Remote Art Studio Careers:")
                print("1. Behaviour Interactive (Montreal): https://careers.behaviour.com/")
                print("2. Digital Extremes (Ontario/Remote): https://www.digitalextremes.com/careers")
                print("3. Ubisoft Montreal: https://www.ubisoft.com/en-us/company/careers")
                print("4. Moon Studios (100% Remote): https://moongamestudios.com/jobs/")
                print("5. The Coalition (Vancouver): https://thecoalitionstudio.com/careers/")
                print("6. Riot Games (Remote/Hub): https://www.riotgames.com/en/work-with-us/jobs")

        elif choice == "5":
            if os.path.exists(CSV_PATH):
                with open(CSV_PATH, "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for i, row in enumerate(reader):
                        if i == 0:
                            print(f"\n[HEADER] {' | '.join(row[:4])} ...")
                        else:
                            print(f"[{i}] {' | '.join(row[:3])} ({row[6]})")
            else:
                print("CSV file not found.")

        elif choice == "6":
            print("Goodbye and good luck with your job hunt!")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        cfg = load_config()
        if cmd == "score" and len(sys.argv) > 2:
            path = sys.argv[2]
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                res = score_job_listing(content)
                print(json.dumps(res, indent=2))
        elif cmd == "apply" and len(sys.argv) > 3:
            res = generate_ats_answers(sys.argv[2], sys.argv[3], "", cfg)
            print(json.dumps(res, indent=2))
        elif cmd == "export":
            print(f"CSV available at: {CSV_PATH}")
        else:
            interactive_cli()
    else:
        interactive_cli()
