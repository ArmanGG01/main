# bot.py
class ChatBot:
    def __init__(self):
        self.name = "Spacy ChatBot"
        self.nlp_processor = NLPProcessor()  # Anda harus mengimpor NLPProcessor dari nlp_processor.py
        
    def respond(self, user_input):
        response = "Maaf, saya tidak mengerti."
        
        doc = self.nlp_processor.process_input(user_input)
        
        for token in doc:
            if token.pos_ == "VERB":
                response = "Saya melihat Anda ingin " + token.text
                break
        
        return response
