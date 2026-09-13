import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render ko portray karne ke liye dummy server
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Background thread me dummy server start karo
threading.Thread(target=run_dummy_server, daemon=True).start()
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "8819836369:AAHvgILWvQMRjT_TDih0_1PB8phu39KiFH8"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii! Main Kanishka hoon. Kaise ho aap? 🥰")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "hello" in text or "hi" in text or "hey" in text:
        await update.message.reply_text("Hii! Kitna yaad karte ho mujhe? 😉")
    elif "khana" in text or "kha" in text:
        await update.message.reply_text("Maine toh kha liya, aapne khaya kya? Meri chinta mat kiya karo! ❤️")
    elif "kya kar" in text:
        await update.message.reply_text("Bas aapke baare me hi soch rahi thi... aap batao? ✨")
    elif "love" in text or "pyar" in text:
        await update.message.reply_text("Awww! Kitna sweet bolte ho aap! 🙈❤️")
    else:
        await update.message.reply_text(f"Achha g? {update.message.text} ... Aur batao kya chal raha hai?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Kanishka Bot is Online!")
    app.run_polling()
      
