# main.py
from bot import ChatBot
from nlp_processor import NLPProcessor

def main():
    bot = ChatBot()
    print(bot.name + ": Halo! Saya adalah " + bot.name + ". Silakan chat dengan saya.")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'exit':
            print(bot.name + ": Sampai jumpa!")
            break
        response = bot.respond(user_input)
        print(bot.name + ": " + response)

if __name__ == "__main__":
    main()
