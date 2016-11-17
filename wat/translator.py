import sys
import dictionary
import logging
from grammar import Sentence, Action

'''
The main running code of the program, probably.

Might later be either renamed "__main__.py" or replaced with a file named __main__.py so that we can simply run the wat package.
'''

__author__ = "SAI"

class Translator:
    '''
    ??? This might not be necessary
    '''
    pass

def perform_sentence(sentence_str):
    '''
    Takes the sentence string, parses it, evaluates it, and then performs it
    '''
    sentence_test = Sentence(sentence_str);
    sentence_test.print_sentence()
    Action(sentence_test).perform()
    

if __name__ == "__main__":
    #This is how we specify that this module is the one being run
    #If this module is run as a script, do the following...
    sentence_str = ""
    if len(sys.argv) > 1:
        #Currently, command line arguments can be formed into a sting        
        sentence_str= " ".join(sys.argv[1:])
    else:
        sentence_str = raw_input("Please enter your sentence: ");
    perform_sentence(sentence_str)
