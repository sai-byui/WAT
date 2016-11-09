import logging
import os
import re

'''
This code contains how the Words in a sentence are parsed and loaded,
so that Word subclasses can be identified from a sentence string.
'''

__author__="SAI"

ADVERB = "adverb"
ADJECTIVE = "adjective"
VERB = "verb"
NOUN = "noun"
CDATA = "cdata"
CDWORD = "cword"
UNDEFINED = "(undefined)"
'''
These are constants that define the role of each word. Considering changing
them to bitmasks so that one word could have multiple definitions.
Because otherwise, any homonyms would overwrite one another in the 
dictionary
'''

#logging.basicConfig(level=logging.DEBUG)

_wordLogger = logging.getLogger(__name__)
'''
Used for debugging, mostly to list words that have been added to the
dictionary
'''

class _WordTracker(type):
    '''
    The metaclass for the Word class. It catches when it is subclassed
    and adds the subclass to the dictionary
    '''
    
    
    _word_dictionary = {}
    '''
    The dictionary, hashing from the lowercase name of a Word subclass to
    that subclass
    '''
    def __init__(cls, name, bases, clsdict):
        if len(cls.mro()) > 2:
            _WordTracker.add_word(cls,name)
        super(_WordTracker, cls).__init__(name, bases, clsdict)
        
    @classmethod
    def add_word(cls,wordcls,name=None):
        if None == name:
            name = wordcls.__name__
        name = name.lower()
        _wordLogger.info("Word found: " + name)
        _WordTracker._word_dictionary[name] = wordcls

def WordType(wordtype):
    '''
    This is a decorator for a class used to define the class word type,
    which would be the default word type of all instances of the class
    
    Usage: 
    @WordType(NOUN)
    class noun:
    ...

    wordtype > The type of the word for the class
    '''
    def modifyWordTypeTo(cls):
        cls._class_word_type = wordtype
        return cls    
    return modifyWordTypeTo
        
class Word:
    '''
    The Word class, subclassing this adds it to the dictionary
    '''
    _class_word_type = UNDEFINED
    __metaclass__ = _WordTracker
    '''
    This global variable makes it so that WordTracker can modify this
    class and it's subclasses. It is used to identify when this class
    is subclassed
    '''
    
    @classmethod
    def ignore(cls,scls):
        '''
        This creates an annotation so that some word subclasses
        are not added to the dictionary (For example, CData below

        syntax is just put @Word.ignore before the word to ignore
        '''
        del _WordTracker._word_dictionary[scls.__name__.lower()]
        #It is added to the dictionary before this function is called.
        #So we have to remove the word from the dictionary
        _wordLogger.info("Ignoring:   " + scls.__name__) #logs it
        return scls

    
    @staticmethod
    def parse(word_string):
        '''
        This function is called in sentence. It turns a word string
        into an object of the correct class
        '''
        if CData.regex.match(word_string):
            if CDWord.word_regex.match(word_string):
                return CDWord(word_string)
            #If it is CData, it is not in the dictionary
            return CData(word_string)
        elif _WordTracker._word_dictionary:
            word = _WordTracker._word_dictionary.get( \
                        word_string.lower(),Word)()
            #Gets class from dictionary and initializes it
            #Default to "Word", with undefined word type
            return word
            
        
    def __init__(self,word_type=None):
        '''
        Currently just sets the type of the word.
        Might want a new method to specify this since
        python calling super initializers is not as easy
        as in other languages, and we'll do it A LOT.
        '''
        if None == word_type:
            word_type = self.__class__._class_word_type
        self._word_type = word_type

    #This is where the word is evaluated to read data to
    #build the Action object
    def evaluate(self,sentence):
        '''
        Should evaluate the word, so that a complete idea is presented
        when an Action is made from a sentence
        (E.G. Sentence 'Create class "Foo"' would evaluate Create and then
        class would read in the next word "Foo" as the class name)
        '''
        pass

    def word_type(self):
        '''
        returns the type of the word
        '''
        if None == self._word_type:
            self._word_type = self.__class__._class_word_type
        return self._word_type
    
    def print_word_type(self):
        '''
        Prints out the type of the word
        '''
        print(self._word_type)
        return

    def to_str(self):
        '''
        Returns a string representation of this word.
        For CDATA, it is the information between the quotes
        For UNDEFINED, it returns (undefined)
        For most words, it is the class name
        '''
        if(self._word_type != UNDEFINED):
            return self.__class__.__name__
        return UNDEFINED
    
@Word.ignore
@WordType(CDATA)
class CData(Word):
    '''
    Creates a subclass of word that handles character data information
    This class is not really a word, but is like a type of word, 
    so it is not added to the dictionary
    '''
    regex = re.compile("^(\".*\"|\'.*\')$")
    '''
    This regex determines if information provided is character data
    '''
    def __init__(self,value):
        '''
        Overwrites the super constructor
        sets type to CDATA and saves the second argument as the character
        data.
        '''
        super(self.__class__,self).__init__(CDATA)
        self.str = value[1:-1]

    def to_str(self):
        '''
        Modifies to_str to return the character data information rather
        than the class name.
        '''
        return self.str;

@Word.ignore
@WordType(CDWORD)
class CDWord(Word):
    '''
    CData that contains only one word.
    '''

    def __init__(self,value):
        '''
        Overwrites the super constructor
        sets type to CDWORD and saves the second argument as the character
        data.
        '''
        super(self.__class__,self).__init__(CDWORD)
        self.str = value[1:-1]
    
    word_regex = re.compile("^(\"\S+\"|\'\S+\')$")
    name_regex = re.compile("^(\"\w\S*\"|\'\w\S*\')$")

    def to_str(self):
        '''
        Modifies to_str to return the character data information rather
        than the class name.
        '''
        return self.str;
