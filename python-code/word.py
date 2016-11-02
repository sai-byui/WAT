import os


ADVERB = "adverb"
ADJECTIVE = "adverb"
VERB = "verb"
NOUN = "noun"
CDATA = "cdata"
UNDEFINED = "UNDEFINED"


class _WordTracker(type):
    _word_dictionary = {}
    def __init__(cls, name, bases, clsdict):
        if len(cls.mro()) > 2:
            print("Word added: " + name)
            _WordTracker._word_dictionary[name.lower()] = cls
        super(_WordTracker, cls).__init__(name, bases, clsdict)

class Word:
    __metaclass__ = _WordTracker
    @staticmethod
    def parse(word_string):
        return _WordTracker._word_dictionary[word_string.lower()]()
        
    def __init__(self,word_type=UNDEFINED):
        self.__word_queue = word_type
        self.__word_type = word_type

    #This is where the word is evaluated to read data to
    #build the Action object
    def evaluate(self,sentence):
        pass

    def print_word_type(self):
        print(self.__word_type)

#test = Word()

#test.printSomething()
