#!/usr/bin/env python3
"""
Main Telegram Bot File
Handles all bot commands and interactions
"""

import os
import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from modules.database import Database
from modules.game_logic import GameManager
from modules.keyboards import KeyboardManager
from modules.betting import BettingSystem

class TicTacToeBot:
    def __init__(self, token):
        self.token = token
        self.db = Database()
        self.games = GameManager()
        self.keyboards = KeyboardManager()
        self.betting = BettingSystem()
        
    async def start(self, update, context):
        """Handle /start command"""
        # ... implementation
        
    async def handle_callback(self, update, context):
        """Handle inline button clicks"""
        # ... implementation
        
    # ... other methods

def main():
    """Main function to run the bot"""
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    TOKEN = os.getenv('BOT_TOKEN')
    
    if not TOKEN:
        logger.error("BOT_TOKEN not found in .env file")
        sys.exit(1)
    
    # Create bot instance
    bot = TicTacToeBot(TOKEN)
    
    # Build application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("newgame", bot.new_game))
    application.add_handler(CommandHandler("balance", bot.check_balance))
    application.add_handler(CallbackQueryHandler(bot.handle_callback))
    
    # Start bot
    logger.info("🤖 Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
