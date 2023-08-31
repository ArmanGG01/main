# main.py
from telegram_bot import TelegramBot

def main():
    bot_token = "6396387965:AAHX5skZodxk19t44JztLMEwQxk-l0Qyznk"  # Gantikan dengan token bot Anda
    telegram_bot = TelegramBot(bot_token)
    print("Bot sedang berjalan di platform Telegram...")
    telegram_bot.start_polling()

if __name__ == "__main__":
    main()
