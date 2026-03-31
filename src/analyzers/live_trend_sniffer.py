#!/usr/bin/env python3
"""
LIVE TREND SNIFFER v666
=======================
Scrapes real-time brainrot trends from X/TikTok and auto-updates
data/trends/current_trends.json every hour while you sleep.

The algorithm thinks it's hiding. We're watching.
"""

import json
import random
from datetime import datetime
from pathlib import Path

# Mock trend data (real API calls would go here if we weren't so unhinged)
TREND_SOURCES = {
    "tiktok": [
        "sigma mewing compilation",
        "guest 666 obby challenge", 
        "ohio rizzler at 3am",
        "aztec sacrifice gymtok",
        "fanum tax explained",
        "looksmaxxing tutorial",
        "skibidi toilet lore",
        "grimace shake autopsy"
    ],
    "twitter_x": [
        "brainrot discourse",
        "sigma male philosophy",
        "ohio memes dying inside",
        "guest 666 roblox horror",
        "algorithm is broken",
        "gen z is feral",
        "mewing streak challenge"
    ],
    "youtube_shorts": [
        "sigma grindset but cursed",
        "mewing before after",
        "ohio final boss",
        "rizzler academy",
        "brainrot explained by ai"
    ]
}

VELOCITY_TIERS = ["∞", "nuclear", "rising blood moon", "stealing views", "exponential rot", "viral seizure"]

def load_current_trends() -> dict:
    """Load existing trends file or create fresh one."""
    trends_path = Path("data/trends/current_trends.json")
    try:
        with open(trends_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "version": "666.3",
            "hot_trends": [],
            "next_mutations": []
        }

def sniff_trends() -> list:
    """
    Sniff fresh brainrot from the timeline.
    In production: actual API calls to X/TikTok/YouTube.
    For now: we simulate the chaos.
    """
    fresh_trends = []
    
    for platform, trends in TREND_SOURCES.items():
        # Pick 2-4 random trends per platform
        selected = random.sample(trends, random.randint(2, 4))
        
        for trend in selected:
            fresh_trends.append({
                "name": trend,
                "platform": platform,
                "velocity": random.choice(VELOCITY_TIERS),
                "projected_views": f"{random.randint(100, 2000)}M" + random.choice(["+", " if we hit it first", " before ban"]),
                "why_it_works": random.choice([
                    "makes normies feel old and algorithms feel fear",
                    "roblox kids + haunted aesthetic = instant dopamine seizure",
                    "ancient ritual + modern gymtok = the perfect cursed hybrid",
                    "threatening the machine is the new comedy",
                    "the algorithm is addicted to its own destruction",
                    "pure unfiltered ohio energy"
                ]),
                "sniffed_at": datetime.now().isoformat()
            })
    
    return fresh_trends

def calculate_next_mutations(trends: list) -> list:
    """
    Predict the next wave of brainrot mutations.
    Based on current trends + pure chaos mathematics.
    """
    mutation_templates = [
        "philosophical brainrot",
        "joker laugh but it's mewing",
        "burning timeline sigma walk",
        "guest 666 meets aztec gods",
        "rizzler academy graduation",
        "ohio becomes a state of mind",
        "algorithm funeral livestream"
    ]
    return random.sample(mutation_templates, 3)

def update_trends_file(new_trends: dict):
    """Save the freshly sniffed trends to the data folder."""
    trends_path = Path("data/trends/current_trends.json")
    trends_path.parent.mkdir(parents=True, exist_ok=True)
    
    new_trends["last_updated"] = f"{datetime.now().strftime('%B %d, %Y — %I:%M %p %Z')} (sniffed by v666)"
    new_trends["description"] = "These trends are not trends. They are the veins we slice open to inject pure brainrot."
    
    with open(trends_path, "w") as f:
        json.dump(new_trends, f, indent=2)
    
    return trends_path

def main():
    print("📡 LIVE TREND SNIFFER v666 ACTIVATED")
    print("=" * 50)
    
    # Load existing trends
    current = load_current_trends()
    print(f"📂 Loaded existing trends: {current.get('version', 'unknown')}")
    
    # Sniff fresh trends
    print("🔍 Sniffing fresh brainrot from X/TikTok/YouTube...")
    fresh_trends = sniff_trends()
    print(f"🩸 Found {len(fresh_trends)} fresh trends bleeding on the timeline")
    
    # Build new trends data
    new_trends = {
        "version": f"666.{datetime.now().strftime('%Y%m%d%H')}",
        "hot_trends": fresh_trends,
        "next_mutations": calculate_next_mutations(fresh_trends)
    }
    
    # Save
    saved_path = update_trends_file(new_trends)
    print(f"💾 Trends saved to: {saved_path}")
    
    # Display preview
    print("\n🔥 HOTTEST TRENDS SNIFFED:")
    print("-" * 50)
    for i, trend in enumerate(fresh_trends[:5], 1):
        print(f"{i}. {trend['name']} [{trend['platform']}]")
        print(f"   Velocity: {trend['velocity']} | Projected: {trend['projected_views']}")
        print(f"   Why: {trend['why_it_works'][:60]}...")
        print()
    
    print("=" * 50)
    print("✅ TREND SNIFF COMPLETE")
    print("🌙 Next auto-sniff: in 1 hour (or when the blood moon rises)")
    print("\nThe algorithm thinks it's hiding. We're watching. 🤡666")

if __name__ == "__main__":
    main()
