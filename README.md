
# Golubhai Premium Telegram Bot

A Telegram bot that:
- Sends binary trading signals
- Requires users to subscribe (15 days ₹199 / 30 days ₹299)
- Admin can add users and broadcast signals

## Commands

- `/start` — Show subscription info or welcome message
- `/signal` — Send test signal (if subscribed)
- `/adduser <user_id> <days>` — Admin only: add a user for specific days
- `/broadcast <message>` — Admin only: send message to all active users

## Setup on Render.com

1. Create new service (Background Worker)
2. Connect your GitHub or upload manually
3. Set environment variable:
    - `BOT_TOKEN=your_telegram_bot_token`
4. Set `Start Command`: `python bot.py`
5. Deploy and run 24x7!

Made with ❤️ by Golubhai.
