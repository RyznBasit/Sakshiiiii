import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8514622772:AAHDltQv-zhoRPH0rJBxUBaXAa_8FAJLZwE"
GEMINI_KEY = "AIzaSyBan36vmOg5jkoAGnyzBthdG3bY1d_kbpo"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    res = model.generate_content(msg)
    await update.message.reply_text(res.text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
