from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ...
# Fungsi yang akan dipanggil saat /start diberikan
def start(update, context):
    update.message.reply_text("Halo! Aku adalah bot gabut yang keren. Mari kita mulai obrolan!")

# Fungsi yang akan dipanggil saat pengguna mengirim pesan teks
def respond_to_text(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    response = generate_response(user_message)
    update.message.reply_text(response)

# Fungsi untuk menghasilkan respons berdasarkan pesan pengguna
def generate_response(user_message):
    if "halo" in user_message:
        return "Halo juga! Ada yang bisa aku bantu?"
    elif "apa kabar?" in user_message:
        return "Aku baik-baik saja, terima kasih! Bagaimana denganmu?"
    elif "lagi apa?" in user_message:
        return "Aku sedang di sini siap melayani kamu! Kamu sendiri?"
    else:
        return "Hmm, maaf aku belum sepenuhnya mengerti apa yang kamu maksud."

def main():
    # Ganti "TOKEN_ANDA" dengan token bot Telegram Anda
    updater = Updater(token="6396387965:AAHVSjgaqZPYZ6U4tdceG_-b2CEzDi2EtG8", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
