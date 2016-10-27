import os


ADVERB = "adverb"
ADJECTIVE = "adverb"
VERB = "verb"
NOUN = "noun"

class Word:
    
    def __init__(self,word_type=""):
        self.word_type = word_type

    def print_word_type(self):
        print self.word_type

#test = Word()

#test.printSomething()
