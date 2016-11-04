import os
import re
from word import Word,CDATA,CDWORD
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
    delim = re.compile("\"|\'")
    '''
    This is a delimiter used in parsing, to identify cdata and cdata words
    '''
    
    def __init__(self, sentence_str):
        '''
        parses the sentence_str into a sentence
        '''
        #strsplit = re.split(" ")
        
        strsplit = delim.split(sentence_str)
        word_queue = []
        for i in xrange(0,len(strsplit)):
            if 0 == i % 2:
                if strsplit[i].strip() != "":
                    word_queue.extend(strsplit[i].strip().split(" "))
            else:
                if strsplit[i] != "":
                    word_queue.append("\"" + strsplit[i] + "\"")
        
        #word_queue = sentence_str.split(" ")
        
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
                wrd = " \"%s\"" % wrd
            elif word.word_type() == CDWORD:
                #For now, CDWORDS are kept separate from CDATA
                #when printed they have '' 's instead of ""
                #This can change and doesn't affect how they are parsed
                wrd =  " \'%s\'" % wrd
            elif not firstWord:
                wrd = " " + wrd.lower()
            firstWord = False
            sentence += wrd
        sentence += "."
        print(sentence)

#delim = re.compile("\"|\'")

if "__main__" == __name__:
    str = raw_input("Parse test:")
    strsplit = Sentence.delim.split(str)
    for str in strsplit:
        print("*" + str)
    wordsplit = []
    for i in xrange(0,len(strsplit)):
        if 0 == i % 2:
            wordsplit.extend(strsplit[i].strip().split(" "))
        else:
            wordsplit.append("\"" + strsplit[i] + "\"")

    print(".".join(wordsplit))

