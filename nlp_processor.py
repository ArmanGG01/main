# nlp_processor.py
import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def process_input(self, user_input):
        doc = self.nlp(user_input)
        return doc
