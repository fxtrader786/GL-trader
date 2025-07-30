
import json
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN", "8267757473:AAFjpLzzEb2gFqvVgz-mDBgfMiHa6kPubEA")
ADMIN_ID = 5747124136
UPI_ID = "7747811910@ybl"

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def check_subscription(user_id):
    data = load_data()
    if str(user_id) in data:
        expiry = datetime.datetime.strptime(data[str(user_id)], "%Y-%m-%d")
        return datetime.datetime.now() <= expiry
    return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if check_subscription(user_id):
        await update.message.reply_text("✅ Welcome back to Golubhai Premium Bot!")
    else:
        await update.message.reply_text(
            "👋 Welcome to Golubhai Premium Bot!

"
            "🔒 To activate access:
"
            f"➤ 15 Days – ₹199
➤ 30 Days – ₹299

"
            f"📤 Pay via UPI: {UPI_ID}

"
            "📩 After payment, send screenshot to @terausername
"
        )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if check_subscription(user_id):
        await update.message.reply_text("📈 EUR/USD OTC: CALL
✅ Win")
    else:
        await update.message.reply_text("❌ Subscription expired. Use /start to renew.")

async def adduser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        user_id = context.args[0]
        days = int(context.args[1])
        expiry = datetime.datetime.now() + datetime.timedelta(days=days)
        data = load_data()
        data[str(user_id)] = expiry.strftime("%Y-%m-%d")
        save_data(data)
        await update.message.reply_text(f"✅ User {user_id} added till {expiry.strftime('%Y-%m-%d')}")
    except:
        await update.message.reply_text("❗ Usage: /adduser user_id days")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    data = load_data()
    msg = " ".join(context.args)
    count = 0
    for user in data:
        if check_subscription(user):
            try:
                await context.bot.send_message(chat_id=int(user), text=msg)
                count += 1
            except:
                continue
    await update.message.reply_text(f"✅ Broadcast sent to {count} users.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("adduser", adduser))
app.add_handler(CommandHandler("broadcast", broadcast))

if __name__ == "__main__":
    app.run_polling()
