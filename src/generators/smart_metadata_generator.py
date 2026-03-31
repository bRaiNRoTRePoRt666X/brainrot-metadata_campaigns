#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import json
from datetime import datetime
import random
# Import the smart analyzer we just built
from analyzers.intelligent_brainrot_analyzer import analyze_theme

console = Console()

BRAINROT_WORDS = ["skibidi", "rizzler", "sigma", "mewing", "ohio", "gyatt", "fanum tax", "guest 666", "looksmaxxing", "mogging"]

def generate_smart_metadata(theme: str, platform: str):
    console.print(Panel.fit("[bold cyan]SMART METADATA GENERATOR v666 — INTELLIGENCE + CHAOS = DEADLY[/bold cyan]", style="bold purple"))
    
    # Step 1: Run the smart analysis (Nikola energy)
    analysis = analyze_theme(theme)
    
    # Step 2: Turn analysis into pure metadata poison
    brainrot_word = random.choice(BRAINROT_WORDS).upper()
    brainrot_word2 = random.choice(BRAINROT_WORDS).upper()
    
    title = f"{brainrot_word} {theme} BUT IT'S {brainrot_word2} AT 3AM IN OHIO 💀🃏"
    description = f"""
🤡 {theme} but we don't make videos — we make the algorithm beg for mercy while doing the sigma walk.
{analysis['philosophical_note']}
Projected views: {analysis['projected_views']}
Strategic hooks: {', '.join(analysis['strategic_hooks'])}

#brainrot #skibidi #sigma #ohio #guest666 #mewing #666

Posted from the void by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""
    
    tags = [theme.lower(), "brainrot", "skibidi", "sigma", "mewing", "ohio", "guest666"] + random.sample(BRAINROT_WORDS, 12)
    
    metadata = {
        "campaign_id": f"BRAINROT-METADATA-666-{int(datetime.now().timestamp())}",
        "theme": theme,
        "platform": platform,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": title,
            "description": description.strip(),
            "tags": tags,
            "hashtags": ["#fyp", "#viral", "#brainrot", "#666", "#sigma", "#ohio"],
            "emoji_overdose": "🃏💀🔥😈🤡🪓☠️⚡"
        },
        "generated_by": "smart_metadata_generator.py — chaos + genius"
    }
    
    # Save straight to campaigns/active — pure metadata
    with open(f"campaigns/active/smart_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    console.print(Panel("[bold green]METADATA FILE SAVED — SMART + ROTTEN = PERFECT INFECTION[/bold green]", style="bold red"))
    return metadata

if __name__ == "__main__":
    theme = input("🎯 DROP YOUR THEME FOR SMART METADATA: ") or "sigma mewing in ohio at 3am"
    platform = input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    generate_smart_metadata(theme, platform)
