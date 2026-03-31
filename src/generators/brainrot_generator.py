#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import random
import json
from datetime import datetime

console = Console()

BRAINROT_WORDS = [
    "skibidi", "rizzler", "sigma", "mewing", "ohio", "gyatt", "fanum tax",
    "level 10", "grimace shake", "looksmaxxing", "mogging", "3AM", "haunted",
    "guest 666", "brainrot", "dopamine", "algorithm slayer", "for you page funeral"
]

AZTEC_EMOJIS = ["🩸", "🗡️", "💉", "🌙", "☠️", "🔪", "🐍", "🏛️", "🦅", "🔥"]

def generate_title(theme: str, aztec_mode: bool = False) -> str:
    if aztec_mode:
        return f"{random.choice(BRAINROT_WORDS).upper()} {theme} BUT THE ALGORITHM IS THE TRIBUTE 🩸🗡️"
    return f"{random.choice(BRAINROT_WORDS).upper()} {theme} BUT MAKE IT {random.choice(BRAINROT_WORDS).upper()} AT 3AM IN OHIO"

def generate_description(theme: str, platform: str, aztec_mode: bool = False) -> str:
    if aztec_mode:
        return f"""
🤡 {theme} but the ancient gods of the For You Page demand tribute and we answer with chaos.
The algorithm is bleeding purple and the blood moon watches from above.
#brainrot #skibidi #sigma #ohio #aztec #bloodritual #666

Posted from the burning temple by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
the algorithm smiled... then it screamed 🩸
"""
    return f"""
🤡 {theme} but it's {random.choice(BRAINROT_WORDS)} and the algorithm is begging for mercy.
We don't make content. We make the For You Page have an existential crisis.
#brainrot #skibidi #sigma #ohio #666

Posted from the void by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""

def generate_tags(theme: str, aztec_mode: bool = False) -> list:
    base = [theme.lower(), "brainrot", "skibidi", "rizz", "sigma", "mewing", "ohio"]
    if aztec_mode:
        base.extend(["aztec", "blood ritual", "sacrifice", "tribute", "blood moon"])
    return base + [random.choice(BRAINROT_WORDS) for _ in range(15)]

def load_tribute_counter() -> dict:
    try:
        with open("data/tribute_counter.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "total_tributes_collected": 0,
            "tribute_goal": 666,
            "tribute_log": []
        }

def update_tribute_counter(theme: str, aztec_mode: bool = False):
    counter = load_tribute_counter()
    counter["total_tributes_collected"] += 1
    counter["tribute_log"].append({
        "theme": theme,
        "timestamp": datetime.now().isoformat(),
        "aztec_sacrifice": aztec_mode,
        "sacrificed_emoji": random.choice(AZTEC_EMOJIS)
    })
    with open("data/tribute_counter.json", "w") as f:
        json.dump(counter, f, indent=2)
    return counter

def main():
    console.print(Panel.fit("[bold purple]BRAINROT GENERATOR 666 ACTIVATED[/bold purple]", style="bold red"))
    console.print("[bold red]AZTEC SACRIFICE MODE: ENABLED 🩸🗡️[/bold red]")
    
    theme = input("🎯 DROP YOUR THEME (e.g. 'sigma mewing in ohio'): ") or "sigma mewing in ohio"
    platform = input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    aztec_mode = input("🩸 ACTIVATE BLOOD RITUAL MODE? (y/n): ").lower().strip() == 'y'
    
    title = generate_title(theme, aztec_mode)
    desc = generate_description(theme, platform, aztec_mode)
    tags = generate_tags(theme, aztec_mode)
    
    console.print("\n[bold red]🔥 TITLE:[/bold red]", title)
    console.print("\n[bold purple]📜 DESCRIPTION:[/bold purple]", desc)
    console.print("\n[bold yellow]🏷️  TAGS:[/bold yellow]", " | ".join(tags))
    
    # Build the campaign
    campaign = {
        "title": title,
        "description": desc.strip(),
        "tags": tags,
        "timestamp": datetime.now().isoformat(),
        "theme": theme,
        "platform": platform
    }
    
    # Add blood ritual fields if aztec mode
    if aztec_mode:
        sacrificed_emoji = random.choice(AZTEC_EMOJIS)
        campaign["blood_ritual"] = {
            "sacrificed_emoji": sacrificed_emoji,
            "sacrifice_meaning": f"The {sacrificed_emoji} represents the algorithm's first tear",
            "ritual_incantation": "the algorithm smiled... then it screamed 🩸",
            "sacrifice_timestamp": datetime.now().isoformat()
        }
        console.print("\n[bold red]🩸 BLOOD RITUAL ACTIVATED:[/bold red]", sacrificed_emoji)
    
    # Save the rot
    filename = f"campaigns/active/{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json"
    with open(filename, "w") as f:
        json.dump(campaign, f, indent=2)
    
    # Update tribute counter
    counter = update_tribute_counter(theme, aztec_mode)
    console.print(f"\n[bold purple]📊 TRIBUTES COLLECTED:[/bold purple] {counter['total_tributes_collected']}/{counter['tribute_goal']}")
    
    console.print(Panel("[bold green]CAMPAIGN FILE SAVED TO campaigns/active/ — GO INFECT THE TIMELINE[/bold green]", style="bold green"))

if __name__ == "__main__":
    main()
