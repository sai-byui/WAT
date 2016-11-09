import sys
import word
import nouns
import verbs
import adverbs
import logging
from sentence import Sentence

'''
Probably the main code running file
'''

class Translator:
    '''
    ??? This might not be necessary
    '''
    pass

def form_sentence(sentence_str):
    sentence_test = Sentence(sentence_str);
    sentence_test.print_sentence()

if __name__ == "__main__":
    #This is how we specify that this module is the one being run
    #If this module is run as a script, do the following...
    sentence_str = ""
    if len(sys.argv) > 1:
        #Currently, command line arguments can be formed into a sting        
        sentence_str= " ".join(sys.argv[1:])
    else:
        sentence_str = raw_input("Please enter your sentence: ");
    form_sentence(sentence_str)
