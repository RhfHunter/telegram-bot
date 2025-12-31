"""
Inline keyboards for Telegram bot
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List, Dict

class KeyboardManager:
    """Manages all inline keyboards"""
    
    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        """Main menu keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("🎮 নতুন গেম", callback_data="menu_new_game"),
                InlineKeyboardButton("💰 ব্যালেন্স", callback_data="menu_balance")
            ],
            [
                InlineKeyboardButton("📊 লিডারবোর্ড", callback_data="menu_leaderboard"),
                InlineKeyboardButton("⚙️ সেটিংস", callback_data="menu_settings")
            ],
            [
                InlineKeyboardButton("❓ সাহায্য", callback_data="menu_help"),
                InlineKeyboardButton("ℹ️ রুলস", callback_data="menu_rules")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def game_board(game_id: str, board_state: List[List[str]]) -> InlineKeyboardMarkup:
        """Tic Tac Toe game board keyboard"""
        keyboard = []
        for i in range(3):
            row = []
            for j in range(3):
                if board_state[i][j] == 'X':
                    text = "❌"
                elif board_state[i][j] == 'O':
                    text = "⭕"
                else:
                    text = "⬜"
                row.append(
                    InlineKeyboardButton(
                        text, 
                        callback_data=f"move_{game_id}_{i}_{j}"
                    )
                )
            keyboard.append(row)
        
        # Add control buttons
        keyboard.append([
            InlineKeyboardButton("🏳️ সমর্পণ", callback_data=f"surrender_{game_id}"),
            InlineKeyboardButton("❌ বাতিল", callback_data=f"cancel_{game_id}")
        ])
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def bet_selection() -> InlineKeyboardMarkup:
        """Bet amount selection keyboard"""
        keyboard = []
        bets = [5, 10, 20, 50, 100]
        
        row = []
        for bet in bets:
            row.append(InlineKeyboardButton(f"{bet} 🪙", callback_data=f"bet_{bet}"))
            if len(row) == 3:
                keyboard.append(row)
                row = []
        
        keyboard.append([
            InlineKeyboardButton("✏️ কাস্টম", callback_data="bet_custom"),
            InlineKeyboardButton("↩️ পিছনে", callback_data="back_main")
        ])
        
        return InlineKeyboardMarkup(keyboard)
