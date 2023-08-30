import telebot
from telebot import types
import random

# Ganti 'TOKEN_BOT_ANDA' dengan token bot yang Anda dapatkan dari BotFather di Telegram
TOKEN = '6396387965:AAHIUuWxTJMfYCrATSXMZOf1a5OI6_km0AM'
bot = telebot.TeleBot(TOKEN)

# Keyboard kustom
keyboard = types.ReplyKeyboardMarkup(row_width=2)
start_button = types.KeyboardButton('/start')
help_button = types.KeyboardButton('/help')
keyboard.add(start_button, help_button)

# Perintah start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Aku adalah bot interaktif. Ketik /help untuk melihat opsi.", reply_markup=keyboard)

# Perintah help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Aku adalah bot yang bisa melakukan hal-hal keren!\n\n" \
                "Pilih salah satu opsi:\n" \
                "/gambar - Kirim gambar acak\n" \
                "/fakta - Kirim fakta menarik\n" \
                "/lelucon - Berikan lelucon lucu"
    bot.reply_to(message, help_text, reply_markup=keyboard)

# Perintah gambar
@bot.message_handler(commands=['gambar'])
def send_image(message):
    images = ["link_gambar1.jpg", "link_gambar2.jpg"]  # Ganti dengan tautan gambar yang sesuai
    random_image = random.choice(images)
    bot.send_photo(message.chat.id, photo=random_image)

# Perintah fakta
@bot.message_handler(commands=['fakta'])
def send_fact(message):
    facts = ["Fakta menarik 1.", "Fakta menarik 2.", "Fakta menarik 3."]
    random_fact = random.choice(facts)
    bot.reply_to(message, random_fact)

# Perintah lelucon
@bot.message_handler(commands=['lelucon'])
def send_joke(message):
    jokes = ["Lelucon lucu 1.", "Lelucon lucu 2.", "Lelucon lucu 3."]
    random_joke = random.choice(jokes)
    bot.reply_to(message, random_joke)

# Tanggapan berdasarkan kata kunci
@bot.message_handler(func=lambda message: 'lucu' in message.text.lower())
def respond_to_keyword(message):
    bot.reply_to(message, "Hehe, memang lucu ya!")

# Menjalankan bot
bot.polling()
