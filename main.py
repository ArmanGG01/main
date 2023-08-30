import telebot

# Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
bot = telebot.TeleBot('6396387965:AAHX5skZodxk19t44JztLMEwQxk-l0Qyznk')

def start(message):
    bot.send_message(message.chat.id, "Halo! Aku adalah bot gabut. Kirimkan pesan apapun dan kita bisa ngobrol santai!")

def handle_message(message):
    if message.text.lower() in ['halo', 'hi', 'hai']:
        user_name = message.from_user.first_name
        response = f"Halo {user_name}! Apa kabar?"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Hmmm... Aku juga tidak terlalu tahu apa yang harus kukatakan. 🤷‍♂️")

def on_start_command(message):
    start(message)

def on_any_message(message):
    handle_message(message)

# Jalankan bot
bot.polling()
