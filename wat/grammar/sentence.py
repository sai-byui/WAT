import os
import re
from word import Word,CDATA,CDWORD

'''
This module handles sentences, which parse strings into words and stores
them. It defines the function of a Sentence object and also an iterator
for it. 

Basically, mostly handles the parsing of string into a sentence, and then
it is evaluated in the Action class.
'''

__author__ = "SAI"

class Sentence:
    '''
    This class serves as a data structure containing all the Word objects
    as they are parsed before they become part of an action.
    '''
    delim = re.compile("\"|\'")
    '''
    This is a delimiter used in parsing, to identify cdata and cdata words
    '''
    
    def __init__(self, sentence_str):
        '''
        parses the sentence_str into a sentence
        '''
        strsplit = Sentence.delim.split(sentence_str)
        word_queue = []
        for i in xrange(0,len(strsplit)):
            if 0 == i % 2:
                if strsplit[i].strip() != "":
                    word_queue.extend(strsplit[i].strip().split(" "))
            else:
                if strsplit[i] != "":
                    word_queue.append("\"" + strsplit[i] + "\"")
        self.__word_queue = [Word.parse(w) for w in word_queue]
        self._word_delim = 0

    def iter(self):
        '''
        Returns sentence iterator. It is an iterator that has been modified
        to allow in-line peeking and popping, so it needs a more public
        method than __iter__(self)
        '''
        return self.__iter__()
    
    def __iter__(self):
        '''
        Returns SentenceIterator for this sentence, going through it
        word by word. See the SentenceIterator class.
        Can be used in for in loops.
        '''
        return SentenceIterator(self)

    def __getitem__(self,index):
        '''
        Overloads the brackets [] operator to return the Word at the given
        index
        '''
        return self.__word_queue[index]

    def size(self):
        '''
        How many words are in the sentence
        '''
        return len(self.__word_queue)

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

class SentenceIterator:
    '''
    An iterator for a sentence. In addition to normal iteration, it also
    has pop and peek methods to check the next word ahead
    '''
    def __init__(self,sentence):
        '''
        Constructor for iterator, taking the sentence to iterate through
        as the only argument.
        '''
        self._sentence = sentence
        self._delim = 0;

    def __iter__(self):
        '''
        Returns itself as an iterator for itself. This way you can use
        the iterator in a for loop but also keep a reference to it for 
        using peek and pop.
        '''
        return self
    
    def next(self):
        '''
        Returns the next word in the sentence, the same as pop except for
        iterator implementation, will raise StopIteration instead of 
        returning None
        '''
        if self.end():
            raise StopIteration
        else:
            return self.pop()

    def end(self):
        '''
        Returns True if the sentence iterator has reached the end,
        False otherwise.
        '''
        if self._sentence.size() <= self._delim:
            return True
        return False
    
    def pop(self):
        '''
        Returns the next word and moves the iterator to the next element
        '''
        ret = self.peek()
        self._delim += 1
        return ret
    
    def peek(self):
        '''
        Returns the next word without moving the iterator to it. This can
        be used to determine if the next word is necessary for evaluating
        the current word.

        E.G., Create Class 'Foo', when Class is evaluated, it peeks ahead.
        If the next word is a CDWord (Like it is in this case, 'Foo'), then
        it adds to to the Class word as a property.
        '''
        return self._sentence[self._delim] if \
            not self.end() else None

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
