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

def generate_title(theme: str) -> str:
    return f"{random.choice(BRAINROT_WORDS).upper()} {theme} BUT MAKE IT {random.choice(BRAINROT_WORDS).upper()} AT 3AM IN OHIO"

def generate_description(theme: str, platform: str) -> str:
    return f"""
🤡 {theme} but it's {random.choice(BRAINROT_WORDS)} and the algorithm is begging for mercy.
We don't make content. We make the For You Page have an existential crisis.
#brainrot #skibidi #sigma #ohio #666

Posted from the void by bRaiNRoTRePoRt666X • {datetime.now().strftime('%B %d, %Y')}
"""

def generate_tags(theme: str) -> list:
    base = [theme.lower(), "brainrot", "skibidi", "rizz", "sigma", "mewing", "ohio"]
    return base + [random.choice(BRAINROT_WORDS) for _ in range(15)]

def main():
    console.print(Panel.fit("[bold purple]BRAINROT GENERATOR 666 ACTIVATED[/bold purple]", style="bold red"))
    theme = input("🎯 DROP YOUR THEME (e.g. 'sigma mewing in ohio'): ") or "sigma mewing in ohio"
    platform = input("📺 Platform (tiktok/yt/reels): ") or "tiktok"
    
    title = generate_title(theme)
    desc = generate_description(theme, platform)
    tags = generate_tags(theme)
    
    console.print("\n[bold red]🔥 TITLE:[/bold red]", title)
    console.print("\n[bold purple]📜 DESCRIPTION:[/bold purple]", desc)
    console.print("\n[bold yellow]🏷️  TAGS:[/bold yellow]", " | ".join(tags))
    
    # Save the rot
    campaign = {
        "title": title,
        "description": desc.strip(),
        "tags": tags,
        "timestamp": datetime.now().isoformat(),
        "theme": theme,
        "platform": platform
    }
    with open(f"campaigns/active/{theme.replace(' ', '_')}_{int(datetime.now().timestamp())}.json", "w") as f:
        json.dump(campaign, f, indent=2)
    
    console.print(Panel("[bold green]CAMPAIGN FILE SAVED TO campaigns/active/ — GO INFECT THE TIMELINE[/bold green]", style="bold green"))

if __name__ == "__main__":
    main()
