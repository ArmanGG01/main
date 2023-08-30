import telebot

# Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
bot = telebot.TeleBot('6396387965:AAHVSjgaqZPYZ6U4tdceG_-b2CEzDi2EtG8')

def start(message):
    bot.send_message(message.chat.id, "Halo! Aku adalah bot gabut yang di ciptakan oleh Arman. Kirimkan pesan apapun dan kita bisa ngobrol santai!")

def handle_message(message):
    user_input = message.text.lower()
    user_name = message.from_user.first_name
    
    if user_input in ['halo', 'hi', 'hai']:
        response = f"Halo {user_name}! Apa kabar?"
    elif user_input == 'apa kabar?':
        response = f"Aku hanya bot, tapi aku baik-baik saja, {user_name}."
    elif user_input == 'siapa kamu?':
        response = "Aku adalah bot gabut, tidak punya identitas yang jelas. 😄"
    elif user_input == 'kenalan':
        response = "perkenalkan nama saya Bot Gabut, lalu nama kamu siapa?"
    elif user_input == 'nama':
        response = f"senang berkenalan dengan {user_name} Mu 😊."
    else:
        response = f"Hmmm... Aku juga tidak terlalu tahu apa yang harus kukatakan, {user_name}. 🤷‍♂️"
        
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['start', 'help'])
def on_start_command(message):
    start(message)

@bot.message_handler(func=lambda message: True)
def on_any_message(message):
    handle_message(message)

# Jalankan bot
bot.polling()
