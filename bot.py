# bot.py
from nlp_processor import NLPProcessor

class ChatBot:
    def __init__(self):
        self.name = "Bot Gabut"
        self.nlp_processor = NLPProcessor()
        
    def respond(self, user_input):
        response = "Maaf, saya tidak mengerti."
        
        words = self.nlp_processor.process_input(user_input)
        if 'siapa' in words:
            response = "Saya hanyalah bot gabut, bukan seseorang."
        
        return response
