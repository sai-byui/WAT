import os
from word import Word,CDATA
from collections import deque

#################################################################
# Sentence Class:
#
# Description: This class serves as a data structure for holding
# pseudo code keywords that will be translated into python code.
#
# Author: SAI
#################################################################

'''
I think python typically uses 3 double/single quotes to indicate a
"docstring"?
'''

__author__ = "SAI"

class Sentence:

    def __init__(self, sentence_str):
        '''
        parses the sentence_str into a sentence
        '''
        word_queue = sentence_str.split(" ")
        #^Should the above be modified to accept multi-word CData as
        #one word?
        self.__word_queue = [Word.parse(w) for w in word_queue]

    def print_sentence(self):
        '''
        Prints out the sentence as it is understood, with CData in quotes
        and undefinied words as "(undefined)"        
        '''
        sentence = ""
        firstWord = True
        for word in self.__word_queue:
            wrd = word.to_str()
            if word.word_type() == CDATA:
                wrd =  " \"%s\"" % wrd
            elif not firstWord:
                wrd = " " + wrd.lower()
            firstWord = False
            sentence += wrd
        sentence += "."
        print(sentence)



