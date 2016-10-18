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

    def __init__(self):
        self.word_queue = deque

    def __init__(self, verb, noun, predicate):
        self.word_queue.append(verb, noun, predicate)



    def print_sentence(self):
        sentence = self.word_queue.__itemsize__
        for words in sentence:
            print self.word_queue.popleft()



def form_sentence():
    verb, noun, predicate = raw_input("Please enter your sentence: ")
    sentence_test = Sentence(verb, noun, predicate)
    sentence_test.print_sentence()



form_sentence()


