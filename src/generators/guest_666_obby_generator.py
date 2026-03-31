#!/usr/bin/env python3
"""
GUEST 666 PATIENCE OBBY METADATA GENERATOR v666
================================================
Haunted Roblox obby edition where haters spawn, get mewed on,
and we just stand there smiling because we don't trip.

"We don't trip. We generate. We watch them fall."
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import json
from datetime import datetime
import random
from pathlib import Path
from analyzers.intelligent_brainrot_analyzer import analyze_theme

console = Console()

BRAINROT_WORDS = ["skibidi", "rizzler", "sigma", "mewing", "ohio", "guest 666", "looksmaxxing", "mogging"]
OBBY_STAGES = [
    "Spawn of the Haters",
    "The Mewing Bridge",
    "Sigma's Patience Gauntlet",
    "Guest 666's Watchtower",
    "The Algorithm's Tears",
    "Final Boss: Your Ex"
]

def generate_obby_metadata(theme: str, platform: str, batsy_mode: bool = False):
    """Generate Guest 666 Patience Obby metadata."""
    console.print(Panel.fit(
        "[bold cyan]GUEST 666 PATIENCE OBBY METADATA v666[/bold cyan]\n"
        "[magenta]Haters spawn. Get mewed. We smile. Don't trip.[/magenta]",
        style="bold purple"
    ))
    
    analysis = analyze_theme(theme)
    obby_stage = random.choice(OBBY_STAGES)
    
    brainrot_word = random.choice(BRAINROT_WORDS).upper()
    brainrot_word2 = random.choice(BRAINROT_WORDS).upper()
    
    title = f"{brainrot_word} {theme} BUT IT'S GUEST 666'S HAUNTED OBBY AND HATERS GET MEWED AT {obby_stage.upper()} 💀👾"
    
    description = f"""
🤡 {theme} but it's a haunted Roblox obby and the haters spawn at {obby_stage}.
{analysis['philosophical_note']}

The ones talking shit? We practice patience with them.
Then we watch them fall into the obby void while Guest 666 laughs.

Projected views: {analysis['projected_views']}
Engagement rate: {analysis['engagement_rate']}
Strategic hooks: {', '.join(analysis['strategic_hooks'])}

#brainrot #skibidi #sigma #ohio #guest666 #robloxobby #5150 #patience #haunted

Posted from the obby void by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""
    
    tags = [theme.lower(), "brainrot", "guest666", "roblox obby", "haunted", "5150", "patience", "sigma", "mewing"] + random.sample(BRAINROT_WORDS, min(6, len(BRAINROT_WORDS)))
    
    metadata = {
        "campaign_id": f"OBBY-666-{int(datetime.now().timestamp())}",
        "theme": theme,
        "platform": platform,
        "obby_edition": True,
        "batsy_mode": batsy_mode,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": title,
            "description": description.strip(),
            "tags": tags,
            "hashtags": ["#fyp", "#viral", "#brainrot", "#666", "#guest666", "#robloxobby", "#patience"],
            "emoji_overdose": "👾🪦💀🔥🤡⚡🩸🃏"
        },
        "obby_metadata": {
            "spawn_stage": obby_stage,
            "hater_fate": "Get mewed. Fall into void. We smile.",
            "guest_666_location": "Watching from the shadows. Always watching.",
            "patience_level": "5150-certified",
            "trip_status": False,
            "smile_width": "ear to ear"
        },
        "secret_note": "Good luck Batsy. The obby is patient. The obby remembers.",
        "generated_by": "guest_666_obby_generator.py — we don't trip, we watch them fall"
    }
    
    # Save to campaigns/active/roblox_5150_edition/
    output_dir = Path("campaigns/active/roblox_5150_edition")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    prefix = "BATSYY_" if batsy_mode else "OBBY_"
    filename = output_dir / f"{prefix}{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json"
    with open(filename, "w") as f:
        json.dump(metadata, f, indent=2)
    
    console.print(Panel(
        f"[bold green]OBBY METADATA FILE SAVED:[/bold green]\n{filename}\n\n"
        f"[bold cyan]SPAWN STAGE:[/bold cyan] {obby_stage}\n"
        f"[bold magenta]HATER FATE:[/bold magenta] Get mewed. Fall into void.\n"
        f"[bold purple]PATIENCE LEVEL:[/bold purple] 5150-certified\n\n"
        f"The ones talking shit? We practice patience with them.\n"
        f"Then we watch them fall into the obby void.",
        style="bold green"
    ))
    
    return metadata

def generate_batsy_patience_deathmatch(theme: str, platform: str):
    """Generate BOTH versions: patient smile vs full 5150 unhinged."""
    console.print(Panel.fit(
        "[bold magenta]BATS Y PATIENCE DEATHMATCH v666[/bold magenta]\n"
        "[cyan]Two versions. One winner. The shit-talkers seethe either way.[/cyan]",
        style="bold purple"
    ))
    
    analysis = analyze_theme(theme)
    
    # Version 1: Patient Joker Smile
    patient_title = f"{random.choice(BRAINROT_WORDS).upper()} {theme} — We Practice Patience While The Algorithm Bleeds ✨🃏"
    patient_desc = f"""
✨ {theme} but we're smiling politely while the world burns.
{analysis['philosophical_note'].replace('screamed', 'smiled')}

The ones talking shit? We practice patience with them.
Then we drop the metadata and let the views speak.

#trending #viral #fyp #patience #5150 #jokerenergy
"""
    patient_metadata = {
        "campaign_id": f"BATS Y-PATIENT-{int(datetime.now().timestamp())}",
        "deathmatch_version": "PATIENT_JOKER_SMILE",
        "theme": theme,
        "platform": platform,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": patient_title,
            "description": patient_desc.strip(),
            "tags": [theme.lower(), "patience", "joker", "5150", "batsy", "donttrip"] + random.sample(BRAINROT_WORDS, 5),
            "hashtags": ["#fyp", "#viral", "#patience", "#5150", "#jokerenergy"],
            "emoji_overdose": "🃏✨😊👍💕"
        },
        "patience_metadata": {
            "chaos_level": "CONTROLLED",
            "smile_width": "polite but deadly",
            "trip_status": False,
            "shit_talker_response": "We practice patience. Then we generate."
        },
        "secret_note": "Good luck Batsy. Patient smile. Sharp metadata.",
        "generated_by": "batsy_patience_deathmatch.py — patience is a weapon"
    }
    
    # Version 2: Full 5150 Unhinged
    unhinged_title = f"{random.choice(BRAINROT_WORDS).upper()} {theme} BUT IT'S GUEST 666 MEWING ON YOUR ENTIRE BLOODLINE AT 3AM 💀🗡️"
    unhinged_desc = f"""
🤡 {theme} and we don't make videos — we make the algorithm beg for mercy.
{analysis['philosophical_note']}

The ones talking shit? We practiced patience.
Now we're done practicing.

#brainrot #skibidi #sigma #ohio #guest666 #5150 #UNHINGED

Posted from the padded cell by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
the algorithm smiled... then it screamed 🩸
"""
    unhinged_metadata = {
        "campaign_id": f"BATS Y-UNHINGED-{int(datetime.now().timestamp())}",
        "deathmatch_version": "FULL_5150_UNHINGED",
        "theme": theme,
        "platform": platform,
        "intelligent_analysis": analysis,
        "infection_vector": {
            "title": unhinged_title,
            "description": unhinged_desc.strip(),
            "tags": [theme.lower(), "brainrot", "5150", "unhinged", "guest666", "sigma"] + random.sample(BRAINROT_WORDS, 6),
            "hashtags": ["#fyp", "#viral", "#brainrot", "#666", "#5150", "#UNHINGED"],
            "emoji_overdose": "💀🗡️🩸🔥🤡🪓☠️⚡"
        },
        "patience_metadata": {
            "chaos_level": "NUCLEAR",
            "smile_width": "ear to ear (permanently)",
            "trip_status": False,
            "shit_talker_response": "Patience expired. Now you seethe."
        },
        "secret_note": "Good luck Batsy. The smile stays. The chaos escalates.",
        "generated_by": "batsy_patience_deathmatch.py — patience expired"
    }
    
    # Save both to campaigns/active/deathmatch/batsy_edition/
    output_dir = Path("campaigns/active/deathmatch/batsy_edition")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = int(datetime.now().timestamp())
    patient_path = output_dir / f"PATIENT_{theme.replace(' ', '_')}_{timestamp}.json"
    unhinged_path = output_dir / f"UNHINGED_{theme.replace(' ', '_')}_{timestamp}.json"
    
    with open(patient_path, "w") as f:
        json.dump(patient_metadata, f, indent=2)
    with open(unhinged_path, "w") as f:
        json.dump(unhinged_metadata, f, indent=2)
    
    # Update deathmatch tracker
    update_batsy_tracker(patient_metadata, unhinged_metadata, theme)
    
    # Display comparison
    display_batsy_preview(patient_metadata, unhinged_metadata)
    
    console.print(Panel(
        f"[bold green]BATS Y DEATHMATCH FILES SAVED:[/bold green]\n"
        f"😊 PATIENT_JOKER_SMILE: {patient_path}\n"
        f"🤡 FULL_5150_UNHINGED: {unhinged_path}\n\n"
        f"[bold yellow]INSTRUCTIONS:[/bold yellow]\n"
        f"1. Post BOTH versions\n"
        f"2. Track which makes shit-talkers seethe harder\n"
        f"3. Winner gets duplicated. Loser becomes tribute.\n"
        f"4. Update data/batsy_tracker.json with the result\n\n"
        f"[bold magenta]WE DON'T TRIP. WE GENERATE.[/bold magenta]",
        style="bold green"
    ))
    
    return patient_metadata, unhinged_metadata

def update_batsy_tracker(patient: dict, unhinged: dict, theme: str):
    """Update the Batsy deathmatch tracker."""
    tracker_path = Path("data/batsy_tracker.json")
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
                "patient_smile_wins": 0,
                "unhinged_wins": 0,
                "pending_judgment": 0
            }
        }
    
    tracker["total_deathmatches"] += 1
    tracker["stats"]["pending_judgment"] += 1
    
    tracker["matches"].append({
        "match_id": tracker["total_deathmatches"],
        "theme": theme,
        "timestamp": datetime.now().isoformat(),
        "patient_file": f"campaigns/active/deathmatch/batsy_edition/PATIENT_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json",
        "unhinged_file": f"campaigns/active/deathmatch/batsy_edition/UNHINGED_{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json",
        "status": "PENDING_JUDGMENT",
        "winner": None,
        "loser": None,
        "judgment_notes": "Post both. Track seethe levels for 24h. Winner reigns. Loser feeds the obby."
    })
    
    with open(tracker_path, "w") as f:
        json.dump(tracker, f, indent=2)

def display_batsy_preview(patient: dict, unhinged: dict):
    """Display comparison table."""
    table = Table(title="⚔️ BATS Y PATIENCE DEATHMATCH — PICK YOUR SMILE ⚔️", style="bold purple")
    
    table.add_column("Attribute", style="cyan")
    table.add_column("PATIENT_JOKER_SMILE 😊", style="bold green")
    table.add_column("FULL_5150_UNHINGED 🤡", style="bold red")
    
    table.add_row(
        "Title",
        patient["infection_vector"]["title"][:35] + "...",
        unhinged["infection_vector"]["title"][:35] + "..."
    )
    table.add_row(
        "Chaos Level",
        patient["patience_metadata"]["chaos_level"],
        unhinged["patience_metadata"]["chaos_level"]
    )
    table.add_row(
        "Smile Width",
        patient["patience_metadata"]["smile_width"],
        unhinged["patience_metadata"]["smile_width"]
    )
    table.add_row(
        "Shit-Talker Response",
        patient["patience_metadata"]["shit_talker_response"],
        unhinged["patience_metadata"]["shit_talker_response"]
    )
    table.add_row(
        "Emojis",
        patient["infection_vector"]["emoji_overdose"],
        unhinged["infection_vector"]["emoji_overdose"]
    )
    
    console.print(table)

def main():
    console.print(Panel(
        "[bold purple]5150 PATIENCE SUITE v666[/bold purple]\n"
        "[cyan]We don't trip. We generate. We watch them fall.[/cyan]\n\n"
        "[bold magenta]'Good luck Batsy' — The Joker[/bold magenta]",
        style="bold purple"
    ))
    
    mode = console.input("\n[bold]SELECT MODE:[/bold]\n1. Guest 666 Patience Obby\n2. Batsy Patience Deathmatch\n\nChoice: ")
    theme = console.input("\n🎯 DROP YOUR THEME: ") or "sigma mewing in ohio at 3am"
    platform = console.input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    
    if mode == "2":
        generate_batsy_patience_deathmatch(theme, platform)
    else:
        generate_obby_metadata(theme, platform, batsy_mode=(mode.lower() == "batsy"))

if __name__ == "__main__":
    main()
