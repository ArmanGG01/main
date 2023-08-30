import telebot

# Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
bot = telebot.TeleBot('6396387965:AAHVSjgaqZPYZ6U4tdceG_-b2CEzDi2EtG8')

def start(message):
    bot.send_message(message.chat.id, "Halo! Aku adalah bot gabut. Kirimkan pesan apapun dan kita bisa ngobrol santai!")

def handle_message(message):
    if message.text.lower() in ['halo', 'hi', 'hai']:
        user_name = message.from_user.first_name
        response = f"Halo {user_name}! Apa kabar?"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Hmmm... Aku juga tidak terlalu tahu apa yang harus kukatakan. 🤷‍♂️")

@bot.message_handler(commands=['start', 'help'])
def on_start_command(message):
    start(message)

@bot.message_handler(func=lambda message: True)
def on_any_message(message):
    handle_message(message)

# Jalankan bot
bot.polling()
