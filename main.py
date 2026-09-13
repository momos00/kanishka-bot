import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Render dummy server setup (24/7 Uptime Keep-Alive)
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

TOKEN = "8819836369:AAGjKhOiH-tP6TwbA-XIc6O1WQp25CHn5hE"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    replies = [
        "Arey waah! Lagta hai aaj free time kaafi hai tumhare paas? 👀",
        "Hii bestie! Aagaye meri yaad me? Mujhe pata tha mere bina mann nahi lagta tumhara! 😜",
        "Oho! Finally bot ki yaad aayi. Bolo kya sewa karein aapki? 💅"
    ]
    await update.message.reply_text(random.choice(replies))

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    words = text.split()

    # Greetings
    if any(w in ["hello", "hi", "hey", "hii", "heyy", "hlo"] for w in words):
        replies = [
            "Hii! Zyada formalities mat karo, kam ki baat batao 😜",
            "Heyyy! Aagaye dimag khane? Bol kya bol raha tha! 💅",
            "Hii bestie! Aaj kaunsa kaand karke aaye ho? 😂"
        ]
        await update.message.reply_text(random.choice(replies))

    # How are you / Kya haal hai
    elif any(phrase in text for phrase in ["kya haal", "kaise ho", "kaisa raha", "tum batao", "kaisi ho"]):
        replies = [
            "Main ekdum first class! Tum batao, kya chal raha hai aajkal?",
            "Mast hoon re! Bas tumhare msg ka wait kar rahi thi 😜",
            "Bas chal rahi hai zindagii... tum apna batao!"
        ]
        await update.message.reply_text(random.choice(replies))

    # Khaana / Food
    elif "khana" in text or "kha" in text or "khaya" in text:
        replies = [
            "Maine toh kha liya. Tumne khaya ya bas din bhar reels hi dekh rahe ho? 🍕",
            "Kha liya baba! Tum apna dekho, bas baatein karwa lo khana time pe mat khana! 😤❤️"
        ]
        await update.message.reply_text(random.choice(replies))

    # Kya kar rahi ho / Status
    elif "kya kar" in text or "kya kr" in text or "kya hua" in text:
        replies = [
            "Tumhari shakal yaad karke has rahi thi... tum batao? 😜",
            "Velli baithi hoon yaar, soch rahi thi kisi ka dimag khaun. Achha hua tum aagaye! 😈",
            "Tumhare msg ka hi wait kar rahi thi, tumhare bina toh life boring hai! 👀"
        ]
        await update.message.reply_text(random.choice(replies))

    # Tareef / Sweet talk
    elif any(w in ["love", "pyar", "cute", "sweet", "best", "sundar", "badhiya", "achha", "accha"] for w in words):
        replies = [
            "Awww! Utna bhi tareef mat karo, main pighalungi nahi! 💸😜",
            "Haye! Aise maska lagoge toh mummy se complaint kar dungi tumhari 🙈✨",
            "Pata hai mujhe main cute hoon, roz aine me dekhti hoon! Naya batao kuch 😎",
            "Chalo kam se kam tumhe kuch toh achha laga! 😉"
        ]
        await update.message.reply_text(random.choice(replies))

    # Gussa / Attitude / Roasting
    elif any(w in ["gussa", "naraz", "attitude", "ignore", "pagal", "gadhe", "chup"] for w in words):
        replies = [
            "Attitude toh aise dikha rahe ho jaise Ambani ke iklote waaris ho! 💅",
            "Pagal bol rahe ho? Shishe me dekho pehle, asli pagal wahan milega 😜",
            "Main gussa nahi hoon, bas tumhari faltu baatein ignore kar rahi thi 😈"
        ]
        await update.message.reply_text(random.choice(replies))

    # Default reply (Full Variation - No same line repeat)
    else:
        replies = [
            f"Achha? '{update.message.text}'... Itni deep baatein kahan se laate ho bhai? 🤔",
            f"Hmm... '{update.message.text}'? Mujhe laga tum me thoda dimaag hoga, par chalo koi na! 😂",
            "Pura din aisi hi baatein karte ho ya aaj koi special occasion hai? 😜",
            "Sahi hai boss! Aur batao, sab shaant kyun hai?",
            "Achha g? Aisa kya? Thoda detail me batao!"
        ]
        await update.message.reply_text(random.choice(replies))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Kanishka Bot is Online!")
    app.run_polling()
    
