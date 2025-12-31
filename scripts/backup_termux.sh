#!/data/data/com.termux/files/usr/bin/bash
# Backup script for Termux

BACKUP_DIR="/sdcard/termux_backups/$(date +%Y%m%d_%H%M%S)"
PROJECT_DIR="$HOME/telegram-bot"

echo "📦 ব্যাকআপ শুরু: $BACKUP_DIR"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup database
if [ -f "$PROJECT_DIR/data/database.db" ]; then
    cp "$PROJECT_DIR/data/database.db" "$BACKUP_DIR/"
    echo "✅ ডাটাবেস ব্যাকআপ করা হয়েছে"
fi

# Backup configuration
cp "$PROJECT_DIR/.env" "$BACKUP_DIR/" 2>/dev/null || true

# Backup logs (last 7 days)
find "$PROJECT_DIR/logs" -name "*.log" -mtime -7 -exec cp {} "$BACKUP_DIR/" \; 2>/dev/null || true

# Create archive
cd "$PROJECT_DIR"
tar -czf "$BACKUP_DIR/full_backup.tar.gz" .

echo "✅ ব্যাকআপ সম্পন্ন: $BACKUP_DIR"
echo "📁 টোটাল ফাইল: $(ls -1 "$BACKUP_DIR" | wc -l)"
