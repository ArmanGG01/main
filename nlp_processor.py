# nlp_processor.py
import nltk
nltk.download('punkt')

class NLPProcessor:
    def __init__(self):
        pass
    
    def process_input(self, user_input):
        words = nltk.word_tokenize(user_input)
        return words
