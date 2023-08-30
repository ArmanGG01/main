import telebot
from telebot import types

# Ganti 'TOKEN_BOT_ANDA' dengan token bot yang Anda dapatkan dari BotFather di Telegram
TOKEN = '6396387965:AAGsdB3_jOaQeCKEDa588UR07vE6aBzYPlo'
bot = telebot.TeleBot(TOKEN)

# ID saluran Anda
CHANNEL_ID = -1001518032494  # Ganti dengan ID saluran Anda

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

# Perintah start dan help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    is_member = check_membership(user_id)
    if is_member:
        welcome_text = "Halo! Aku adalah bot interaktif. Pilih opsi di bawah ini:"
        bot.reply_to(message, welcome_text, reply_markup=keyboard)
    else:
        join_text = "Sebelum menggunakan bot ini, silakan join ke saluran kami."
        bot.reply_to(message, join_text)

# Memeriksa status keanggotaan pengguna dalam saluran
def check_membership(user_id):
    try:
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print("Error:", e)
        return False

# Tanggapan berdasarkan kata kunci
@bot.message_handler(func=lambda message: any(keyword in message.text.lower() for keyword in ['gambar', 'fakta', 'lelucon']))
def respond_to_keyword(message):
    user_id = message.from_user.id
    is_member = check_membership(user_id)
    if is_member:
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

# Menjalankan bot
bot.polling()
