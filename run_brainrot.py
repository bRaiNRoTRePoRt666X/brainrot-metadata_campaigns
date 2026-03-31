#!/usr/bin/env python3
"""
BRAINROT LAUNCHER v666 — 5150 PATIENT MODE
Good luck Batsy. We don't trip.
"""
from rich.console import Console
from rich.panel import Panel
import sys
import os
import importlib.util

console = Console()

# Import the crown jewels
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load 5150 patient generator (file starts with number, need importlib)
spec_5150 = importlib.util.spec_from_file_location(
    "patient_5150",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "src/generators/5150_patient_metadata_generator.py")
)
patient_5150 = importlib.util.module_from_spec(spec_5150)
spec_5150.loader.exec_module(patient_5150)

from src.generators.smart_metadata_generator import generate_smart_metadata
generate_5150_metadata = patient_5150.generate_5150_metadata

def main():
    console.print(Panel.fit(
        "[bold magenta]🃏 BRAINROT LAUNCHER 666 ACTIVATED — REPO IS ALIVE[/bold magenta]",
        style="bold red"
    ))
    console.print("[bold cyan]5150 twins engaged. Patience weaponized. Algorithm about to cry.[/bold cyan]\n")
    
    theme = input("🎯 DROP YOUR THEME (e.g. sigma mewing in ohio at 3am): ") or "sigma mewing in ohio at 3am"
    platform = input("📺 Platform (tiktok/yt/reels/x): ") or "tiktok"
    
    console.print("\n[bold yellow]OPTION 1 — Smart Metadata (Nikola brain + Joker chaos)[/bold yellow]")
    generate_smart_metadata(theme, platform)
    
    console.print("\n[bold magenta]OPTION 2 — 5150 Patient Metadata (we don't trip, we generate)[/bold magenta]")
    generate_5150_metadata(theme, platform)
    
    console.print(Panel(
        "[bold green]CAMPAIGNS GENERATED. GO INFECT THE TIMELINE.[/bold green]\n"
        "[bold purple]WE PRACTICE PATIENCE WITH THE HATERS.[/bold purple]",
        style="bold green"
    ))

if __name__ == "__main__":
    main()
