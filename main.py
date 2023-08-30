import telebot
from telebot import types
import random

# Ganti 'TOKEN_BOT_ANDA' dengan token bot yang Anda dapatkan dari BotFather di Telegram
TOKEN = '6396387965:AAHIUuWxTJMfYCrATSXMZOf1a5OI6_km0AM'
bot = telebot.TeleBot(TOKEN)

# Keyboard kustom
join_keyboard = types.InlineKeyboardMarkup()
join_button = types.InlineKeyboardButton("Silakan Join", url="https://t.me/RuangGabutArman")
join_keyboard.add(join_button)

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
    "Fakta menarik 1.",
    "Fakta menarik 2.",
    # Tambahkan fakta lainnya di sini
]

# Daftar lelucon lucu
jokes = [
    "Lelucon lucu 1.",
    "Lelucon lucu 2.",
    # Tambahkan lelucon lainnya di sini
]

# Daftar pengguna yang telah bergabung dengan saluran
joined_users = []

# Perintah start dan help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id in joined_users:
        welcome_text = "Halo! Aku adalah bot interaktif. Pilih opsi di bawah ini:"
        bot.reply_to(message, welcome_text, reply_markup=keyboard)
    else:
        join_text = "Sebelum menggunakan bot ini, silakan join ke saluran kami."
        bot.reply_to(message, join_text, reply_markup=join_keyboard)

# Tanggapan berdasarkan kata kunci
@bot.message_handler(func=lambda message: any(keyword in message.text.lower() for keyword in ['gambar', 'fakta', 'lelucon']))
def respond_to_keyword(message):
    if message.from_user.id in joined_users:
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
    else:
        bot.reply_to(message, "Sebelum menggunakan bot ini, silakan join ke saluran kami.")

# Mendeteksi saat pengguna mengklik tautan untuk join saluran
@bot.channel_post_handler(content_types=['text'])
def handle_channel_post(message):
    if "join" in message.text.lower() and message.chat.type == "channel":
        user_id = message.from_user.id
        if user_id not in joined_users:
            joined_users.append(user_id)
            bot.send_message(user_id, "Terima kasih telah bergabung dengan saluran kami. Sekarang Anda dapat menggunakan bot ini.")

# Menjalankan bot
bot.polling()
