import telebot
from telebot import types
import random

# Ganti 'TOKEN_BOT_ANDA' dengan token bot yang Anda dapatkan dari BotFather di Telegram
TOKEN = '6396387965:AAHIUuWxTJMfYCrATSXMZOf1a5OI6_km0AM'
bot = telebot.TeleBot(TOKEN)

# Keyboard kustom lebih kecil
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
start_button = types.KeyboardButton('/start')
help_button = types.KeyboardButton('/help')
keyboard.add(start_button, help_button)

# Daftar link gambar acak
image_links = [
    "https://link_gambar1.jpg",
    "https://link_gambar2.jpg",
    # Tambahkan link gambar lainnya di sini
]

# Daftar fakta menarik
facts = [
    "Fakta menarik 1.",
    "Fakta menarik 2.",
    # Tambahkan fakta lainnya di sini
]

# Daftar lelucon lucu
jokes = [
    "Dua Tiga Tutup Botol Mukak Kau Macam Kontol",
    "Btw Aku Sayang Kalian ",
    # Tambahkan lelucon lainnya di sini
]

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
    random_image = random.choice(image_links)
    bot.send_photo(message.chat.id, photo=random_image)

# Perintah fakta
@bot.message_handler(commands=['fakta'])
def send_fact(message):
    random_fact = random.choice(facts)
    bot.reply_to(message, random_fact)

# Perintah lelucon
@bot.message_handler(commands=['lelucon'])
def send_joke(message):
    random_joke = random.choice(jokes)
    bot.reply_to(message, random_joke)

# Menjalankan bot
bot.polling()
