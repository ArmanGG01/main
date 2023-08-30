import telebot

# Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
bot = telebot.TeleBot('6396387965:AAHX5skZodxk19t44JztLMEwQxk-l0Qyznk')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Halo! Aku adalah bot gabut. Kirimkan pesan apapun dan kita bisa ngobrol santai!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() in ['halo', 'hi', 'hai']:
        bot.send_message(message.chat.id, "Halo! Apa kabar?")
    else:
        bot.send_message(message.chat.id, "Hmmm... Aku juga tidak terlalu tahu apa yang harus kukatakan. 🤷‍♂️")

# Jalankan bot
bot.polling()
