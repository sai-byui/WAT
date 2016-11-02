import os
from word import Word
from collections import deque
import nouns
#################################################################
# Sentence Class:
#
# Description: This class serves as a data structure for holding
# pseudo code keywords that will be translated into python code.
#
# Author: SAI
#################################################################

class Sentence:

    # "__" = private
    __word_queue = [] #A list of Word objects (Not an array!)
    
    
    def __init__(self, word_queue):
        self.__word_queue = [Word.parse(w) for w in word_queue]
        
    def print_sentence(self):
#        sentence = self.word_queue.__itemsize__
#        do you mean, itemize? - Testare
        sentence = ""
        firstWord = True
        for word in self.__word_queue:
            
            if firstWord:
                sentence = word.__class__.__name__
                firstWord = False
            else:
                sentence += " " + word.__class__.__name__.lower()
        sentence += "."
        print(sentence)


def form_sentence():
    word_list = raw_input("Please enter " + " your sentence: ").split(" ");
    sentence_test = Sentence(word_list);
    sentence_test.print_sentence()

form_sentence()
