"""
Utility functions
"""

import os
import json
from pathlib import Path
from typing import Any, Dict
from datetime import datetime

def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON file"""
    if Path(file_path).exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(data: Dict[str, Any], file_path: str):
    """Save data to JSON file"""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def format_currency(amount: int) -> str:
    """Format amount as currency"""
    return f"{amount:,} 🪙"

def get_time_now() -> str:
    """Get current time in Bangladesh time"""
    return datetime.now().strftime("%Y-%m-%d %I:%M %p")

def emojify(text: str) -> str:
    """Add emojis to text"""
    emoji_map = {
        "win": "🏆",
        "lose": "💀",
        "draw": "🤝",
        "balance": "💰",
        "game": "🎮",
        "bet": "🎰",
        "error": "❌",
        "success": "✅",
        "warning": "⚠️"
    }
    
    for key, emoji in emoji_map.items():
        if key in text.lower():
            text = f"{emoji} {text}"
            break
    
    return text
