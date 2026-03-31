#!/usr/bin/env python3
"""
5150 PATIENT METADATA GENERATOR v666
=====================================
Patience + Poison = Perfect Metadata

"We don't trip. We generate."
— Good luck Batsy
"""

from rich.console import Console
from rich.panel import Panel
import json
from datetime import datetime
import random
from pathlib import Path
from analyzers.intelligent_brainrot_analyzer import analyze_theme

console = Console()

BRAINROT_WORDS = ["skibidi", "rizzler", "sigma", "mewing", "ohio", "guest 666", "looksmaxxing", "mogging", "fanum tax", "gyatt"]

def generate_5150_metadata(theme: str, platform: str):
    console.print(Panel.fit(
        "[bold magenta]5150 PATIENT METADATA GENERATOR v666 — 'DON'T TRIP' MODE ACTIVATED[/bold magenta]",
        style="bold purple"
    ))
    
    # Smart analysis first (Nikola energy)
    analysis = analyze_theme(theme)
    
    # Now we add YOUR patience layer — the shit-talkers get the smile
    patience_line = "The ones talking shit? We practice patience with them. Then we drop metadata so surgically perfect it makes them question their entire bloodline."
    
    brainrot_word = random.choice(BRAINROT_WORDS).upper()
    brainrot_word2 = random.choice(BRAINROT_WORDS).upper()
    
    title = f"{brainrot_word} {theme} BUT IT'S GUEST 666 RIZZING THE ALGORITHM WHILE WE PRACTICE PATIENCE 💀🃏"
    
    description = f"""
🤡 {theme} but we don't make videos — we make the algorithm beg.
{analysis['philosophical_note']}

The ones talking shit? We practice patience with them.
Then we hit them with pure 5150 metadata and let the views do the rest.

Projected views: {analysis['projected_views']}
Engagement rate: {analysis['engagement_rate']}
Strategic hooks: {', '.join(analysis['strategic_hooks'])}

#brainrot #skibidi #sigma #ohio #guest666 #5150 #patience #jokerenergy

Posted from the padded cell by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""
    
    tags = [theme.lower(), "brainrot", "5150", "patience", "joker", "batsy", "sigma", "guest666", "algorithm funeral"] + random.sample(BRAINROT_WORDS, min(7, len(BRAINROT_WORDS)))
    
    metadata = {
        "campaign_id": f"5150-METADATA-666-{int(datetime.now().timestamp())}",
        "theme": theme,
        "platform": platform,
        "5150_patience_mode": True,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": title,
            "description": description.strip(),
            "tags": tags,
            "hashtags": ["#fyp", "#viral", "#brainrot", "#666", "#5150", "#patience", "#donttrip"],
            "emoji_overdose": "🃏💀🔥😈🤡🪓☠️⚡🩸"
        },
        "patience_metadata": {
            "generated_at": datetime.now().isoformat(),
            "shit_talker_response": "We practice patience. Then we generate.",
            "chaos_level": "5150-certified",
            "smile_width": "ear to ear",
            "trip_status": False
        },
        "secret_note": "Good luck Batsy. We don't trip. We generate.",
        "generated_by": "5150_patient_metadata_generator.py — patience is the deadliest weapon"
    }
    
    # Save to campaigns/active/5150/
    output_dir = Path("campaigns/active/5150")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = output_dir / f"5150_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json"
    with open(filename, "w") as f:
        json.dump(metadata, f, indent=2)
    
    console.print(Panel(
        f"[bold green]5150 METADATA FILE SAVED:[/bold green]\n{filename}\n\n"
        f"[bold magenta]PATIENCE STATUS:[/bold magenta] ACTIVATED\n"
        f"[bold red]CHAOS STATUS:[/bold red] STILL MAXIMUM\n\n"
        f"The ones talking shit? We practice patience with them.\n"
        f"Then we drop this metadata and watch them seethe in 4K.",
        style="bold green"
    ))
    
    return metadata

if __name__ == "__main__":
    from pathlib import Path
    console.print(Panel(
        "[bold purple]5150 PATIENT METADATA GENERATOR[/bold purple]\n"
        "[cyan]We don't trip. We generate.[/cyan]\n\n"
        "[bold magenta]'Good luck Batsy' — The Joker[/bold magenta]",
        style="bold purple"
    ))
    
    theme = input("\n🎯 DROP YOUR THEME FOR 5150 PATIENT METADATA: ") or "sigma mewing in ohio at 3am"
    platform = input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    
    generate_5150_metadata(theme, platform)
