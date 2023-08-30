import telebot
from telebot import types
import random

# Ganti 'TOKEN_BOT_ANDA' dengan token bot yang Anda dapatkan dari BotFather di Telegram
TOKEN = '6396387965:AAHIUuWxTJMfYCrATSXMZOf1a5OI6_km0AM'
bot = telebot.TeleBot(TOKEN)

# Keyboard kustom lebih kecil
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard.add("/gambar", "/fakta", "/lelucon")

# Daftar link gambar acak
image_links = [
    "https://link_gambar1.jpg",
    "https://link_gambar2.jpg",
    # Tambahkan link gambar lainnya di sini
]

# Daftar fakta menarik
facts = [
    "Fakta menarik 1 adalah Yang Buat Bot Ini Sukak Terhadap Kamu Karena dia udah lama mendam perasaan kepada mu ❤",
    "Fakta menarik 2 adalah kamu sama sekali tidak suka terhadap owner saya",
    # Tambahkan fakta lainnya di sini
]

# Daftar lelucon lucu
jokes = [
    "Lelucon lucu 1.",
    "Lelucon lucu 2.",
    # Tambahkan lelucon lainnya di sini
]

# Perintah start dan help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "Halo! Aku adalah bot interaktif. Pilih opsi di bawah ini:"
    bot.reply_to(message, welcome_text, reply_markup=keyboard)

# Tanggapan berdasarkan kata kunci
@bot.message_handler(func=lambda message: any(keyword in message.text.lower() for keyword in ['gambar', 'fakta', 'lelucon']))
def respond_to_keyword(message):
    if 'gambar' in message.text.lower():
        random_image = random.choice(image_links)
        bot.send_photo(message.chat.id, photo=random_image)
    elif 'fakta' in message.text.lower():
        random_fact = random.choice(facts)
        bot.reply_to(message, random_fact)
    elif 'lelucon' in message.text.lower():
        random_joke = random.choice(jokes)
        bot.reply_to(message, random_joke)
    else:
        bot.reply_to(message, "Maaf, aku tidak mengerti perintahmu.")

# Menjalankan bot
bot.polling()
