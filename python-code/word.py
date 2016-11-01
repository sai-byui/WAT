import os


ADVERB = "adverb"
ADJECTIVE = "adverb"
VERB = "verb"
NOUN = "noun"
CDATA = "cdata"
UNDEFINED = "UNDEFINED"

class Word:

    word_type = UNDEFINED;
    
    @staticmethod
    def parse(word_string):
        #Find the right class word for the string
        #Create an instance
        return Word()
    
    def __init__(self,word_type=UNDEFINED):
        selfword_type = word_type

    #This is where the word is evaluated to read data to
    #build the Action object
    def evaluate(self,sentence):
        pass

    def print_word_type(self):
        print self.word_type

#test = Word()

#test.printSomething()
