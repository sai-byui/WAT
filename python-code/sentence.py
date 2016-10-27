import os
from collections import deque

#################################################################
# Sentence Class:
#
# Description: This class serves as a data structure for holding
# pseudo code keywords that will be translated into python code.
#
# Author: SAI
#################################################################


class Sentence:

    word_queue = []
    
    def __init__(self, verb, noun, predicate):
        
        self.word_queue.append(verb)
        self.word_queue.append(noun)
        self.word_queue.append(predicate)
        
    def print_sentence(self):
#        sentence = self.word_queue.__itemsize__
#        do you mean, itemize? - Testare
        sentence = ""
        for word in self.word_queue:
            sentence += word + " "
        sentence += "\b."
        print(sentence)



def form_sentence():
    verb, noun, predicate = raw_input("Please enter " + " your sentence: ").split(
        " ");
    sentence_test = Sentence(verb, noun, predicate)
    sentence_test.print_sentence()



form_sentence()


