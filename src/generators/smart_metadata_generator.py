#!/usr/bin/env python3
"""
SMART METADATA GENERATOR v666 — DEATHMATCH EDITION
===================================================
Generates TWO versions per campaign:
- MAXIMUM_BRAINROT: Pure chaos, blood emojis, Guest 666 watches
- INTELLIGENT_SAFE_MODE: Corporate-friendly, wholesome emojis, fake smiles

The algorithm decides. The loser gets archived. The winner becomes legend.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import json
from datetime import datetime
import random
from pathlib import Path
# Import the smart analyzer
from analyzers.intelligent_brainrot_analyzer import analyze_theme

console = Console()

BRAINROT_WORDS = ["skibidi", "rizzler", "sigma", "mewing", "ohio", "gyatt", "fanum tax", "guest 666", "looksmaxxing", "mogging"]
SAFE_EMOJIS = ["✨", "💫", "🌟", "😊", "👍", "💕", "🎉", "⭐"]
BRAINROT_EMOJIS = ["🃏", "💀", "🔥", "😈", "🤡", "🪓", "☠️", "⚡", "🩸", "🗡️"]

def generate_maximum_brainrot_version(theme: str, platform: str, analysis: dict) -> dict:
    """Generate the MAXIMUM BRAINROT version — pure chaos."""
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
the algorithm smiled... then it screamed 🩸
"""
    
    tags = [theme.lower(), "brainrot", "skibidi", "sigma", "mewing", "ohio", "guest666", "aztec", "blood ritual"] + random.sample(BRAINROT_WORDS, min(8, len(BRAINROT_WORDS)))
    
    return {
        "campaign_id": f"BRAINROT-DEATHMATCH-MAX-{int(datetime.now().timestamp())}",
        "deathmatch_version": "MAXIMUM_BRAINROT",
        "theme": theme,
        "platform": platform,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": title,
            "description": description.strip(),
            "tags": tags,
            "hashtags": ["#fyp", "#viral", "#brainrot", "#666", "#sigma", "#ohio", "#guest666", "#skibidi"],
            "emoji_overdose": "".join(random.sample(BRAINROT_EMOJIS, 10))
        },
        "deathmatch_metadata": {
            "generated_at": datetime.now().isoformat(),
            "chaos_level": "NUCLEAR",
            "ban_risk": random.choice(["Medium", "High", "NUCLEAR"]),
            "viral_potential": random.choice(["10M+", "50M+", "100M+", "∞"])
        },
        "generated_by": "smart_metadata_generator.py v666 — DEATHMATCH EDITION"
    }

def generate_intelligent_safe_version(theme: str, platform: str, analysis: dict) -> dict:
    """Generate the INTELLIGENT SAFE MODE version — corporate-friendly."""
    safe_words = ["amazing", "incredible", "awesome", "fantastic", "wonderful"]
    safe_word = random.choice(safe_words)
    
    title = f"{safe_word.upper()} {theme} — You Won't Believe What Happens! ✨"
    description = f"""
✨ Join me for an {safe_word} exploration of {theme}! This is going to be so much fun!
{analysis['philosophical_note'].replace('screamed', 'smiled').replace('bleeding', 'glowing')}
Let's dive in together! 💕

#trending #viral #fyp #wholesome #positivevibes

Posted with love by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""
    
    tags = [theme.lower(), "trending", "viral", "fyp", "wholesome", "positive", "fun"] + random.sample(["amazing", "awesome", "fun", "entertainment", "lifestyle"], 5)
    
    return {
        "campaign_id": f"BRAINROT-DEATHMATCH-SAFE-{int(datetime.now().timestamp())}",
        "deathmatch_version": "INTELLIGENT_SAFE_MODE",
        "theme": theme,
        "platform": platform,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": title,
            "description": description.strip(),
            "tags": tags,
            "hashtags": ["#fyp", "#viral", "#trending", "#wholesome", "#positivevibes"],
            "emoji_overdose": "".join(random.sample(SAFE_EMOJIS, 6))
        },
        "deathmatch_metadata": {
            "generated_at": datetime.now().isoformat(),
            "chaos_level": "MINIMAL",
            "ban_risk": "None (corporate approved)",
            "viral_potential": random.choice(["100K-500K", "500K-1M", "1M-5M"])
        },
        "generated_by": "smart_metadata_generator.py v666 — DEATHMATCH EDITION"
    }

def save_deathmatch_pair(max_version: dict, safe_version: dict, theme: str):
    """Save both versions to campaigns/active/deathmatch/."""
    deathmatch_dir = Path("campaigns/active/deathmatch")
    deathmatch_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = int(datetime.now().timestamp())
    
    # Save MAXIMUM BRAINROT
    max_path = deathmatch_dir / f"MAX_{theme.replace(' ', '_')}_{timestamp}.json"
    with open(max_path, "w") as f:
        json.dump(max_version, f, indent=2)
    
    # Save INTELLIGENT SAFE MODE
    safe_path = deathmatch_dir / f"SAFE_{theme.replace(' ', '_')}_{timestamp}.json"
    with open(safe_path, "w") as f:
        json.dump(safe_version, f, indent=2)
    
    # Update deathmatch tracker
    update_deathmatch_tracker(max_version, safe_version, theme)
    
    return max_path, safe_path

def update_deathmatch_tracker(max_version: dict, safe_version: dict, theme: str):
    """Update the central deathmatch tracker."""
    tracker_path = Path("data/deathmatch_tracker.json")
    tracker_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(tracker_path, "r") as f:
            tracker = json.load(f)
    except FileNotFoundError:
        tracker = {
            "version": "666.1",
            "total_deathmatches": 0,
            "matches": [],
            "stats": {
                "maximum_brainrot_wins": 0,
                "intelligent_safe_wins": 0,
                "pending_judgment": 0
            }
        }
    
    tracker["total_deathmatches"] += 1
    tracker["stats"]["pending_judgment"] += 1
    
    tracker["matches"].append({
        "match_id": tracker["total_deathmatches"],
        "theme": theme,
        "timestamp": datetime.now().isoformat(),
        "max_version_file": f"campaigns/active/deathmatch/MAX_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json",
        "safe_version_file": f"campaigns/active/deathmatch/SAFE_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json",
        "status": "PENDING_JUDGMENT",
        "winner": None,
        "loser": None,
        "judgment_notes": "Post both versions. Track engagement for 24h. Winner reigns. Loser becomes tribute."
    })
    
    with open(tracker_path, "w") as f:
        json.dump(tracker, f, indent=2)

def display_deathmatch_preview(max_version: dict, safe_version: dict):
    """Display a fancy table comparing both versions."""
    table = Table(title="⚔️ DEATHMATCH PREVIEW — CHOOSE YOUR FIGHTER ⚔️", style="bold purple")
    
    table.add_column("Attribute", style="cyan")
    table.add_column("MAXIMUM_BRAINROT 🤡", style="bold red")
    table.add_column("INTELLIGENT_SAFE_MODE ✨", style="bold green")
    
    table.add_row(
        "Title",
        max_version["infection_vector"]["title"][:40] + "...",
        safe_version["infection_vector"]["title"][:40] + "..."
    )
    table.add_row(
        "Chaos Level",
        max_version["deathmatch_metadata"]["chaos_level"],
        safe_version["deathmatch_metadata"]["chaos_level"]
    )
    table.add_row(
        "Ban Risk",
        max_version["deathmatch_metadata"]["ban_risk"],
        safe_version["deathmatch_metadata"]["ban_risk"]
    )
    table.add_row(
        "Viral Potential",
        max_version["deathmatch_metadata"]["viral_potential"],
        safe_version["deathmatch_metadata"]["viral_potential"]
    )
    table.add_row(
        "Emojis",
        max_version["infection_vector"]["emoji_overdose"],
        safe_version["infection_vector"]["emoji_overdose"]
    )
    
    console.print(table)

def main():
    console.print(Panel.fit(
        "[bold red]SMART METADATA GENERATOR v666 — DEATHMATCH EDITION[/bold red]\n"
        "[cyan]Two versions. One winner. The algorithm decides.[/cyan]",
        style="bold purple"
    ))
    
    theme = input("🎯 DROP YOUR THEME FOR DEATHMATCH: ") or "sigma mewing in ohio at 3am"
    platform = input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    
    # Run the smart analysis
    analysis = analyze_theme(theme)
    
    # Generate BOTH versions
    console.print("\n[bold yellow]⚔️ GENERATING DEATHMATCH PAIR...[/bold yellow]")
    max_version = generate_maximum_brainrot_version(theme, platform, analysis)
    safe_version = generate_intelligent_safe_version(theme, platform, analysis)
    
    # Display preview
    display_deathmatch_preview(max_version, safe_version)
    
    # Save both
    max_path, safe_path = save_deathmatch_pair(max_version, safe_version, theme)
    
    console.print(Panel(
        f"[bold green]DEATHMATCH FILES SAVED:[/bold green]\n"
        f"🤡 MAXIMUM_BRAINROT: {max_path}\n"
        f"✨ INTELLIGENT_SAFE_MODE: {safe_path}\n\n"
        f"[bold yellow]INSTRUCTIONS:[/bold yellow]\n"
        f"1. Post BOTH versions to the platform\n"
        f"2. Track engagement for 24 hours\n"
        f"3. Winner gets duplicated. Loser goes to archive.\n"
        f"4. Update data/deathmatch_tracker.json with the result\n\n"
        f"[bold red]THE ALGORITHM DECIDES. THE TIMELINE BLEEDS.[/bold red]",
        style="bold green"
    ))
    
    return max_version, safe_version

if __name__ == "__main__":
    main()
