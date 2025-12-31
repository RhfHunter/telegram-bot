#!/data/data/com.termux/files/usr/bin/bash
# Termux Setup Script

echo "📱 Termux টিক ট্যাক টো বট সেটআপ শুরু..."

# Update packages
pkg update -y && pkg upgrade -y

# Install required packages
pkg install -y python git curl

# Install Python packages
pip install --upgrade pip
pip install python-telegram-bot python-dotenv

# Create project structure
mkdir -p ~/telegram-bot/{data,logs,modules,assets,scripts,backups}

echo "✅ সেটআপ সম্পন্ন!"
echo "🔧 এখন করুন:"
echo "1. cd ~/telegram-bot"
echo "2. nano .env  # আপনার বট টোকেন যোগ করুন"
echo "3. python bot.py"
