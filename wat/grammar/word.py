import logging
import os
import re

'''
This code contains how the Words in a sentence are parsed and loaded,
so that Word subclasses can be identified from a sentence string, and
then also a function to evaluate the word into it's place in an Action.

Evaluate is an instance method so it can be overwritten in subclasses for
more dynamic behavior.
'''

__author__="SAI"

ADVERB = "adverb"
'''Specifies an adverb word type'''
ADJECTIVE = "adjective"
'''Specifies an adjective word type'''
VERB = "verb"
'''Specifies an verb word type'''
NOUN = "noun"
'''Specifies an noun word type'''
CDATA = "cdata"
'''Specifies a string of multi-word character data'''
CDWORD = "cword"
'''Specifies a string of character data, but only one word'''
UNDEFINED = "(undefined)"
'''
Specifies a word's type is undefined (usually cause it is not a recognized
 word)

These are constants that define the role of each word. Considering changing
them to bitmasks so that one word could have multiple definitions.
Because otherwise, any homonyms would overwrite one another in the 
dictionary. For now we don't have any homonyms though, so there is no need
'''

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
        '''
        Is called when Word is subclassed.
        Adds the name of the class to the dictionary, with a reference
        to the class. If that word already exists, it is overwritten

        If the subclass has a @Word.ignore decorator, it will remove
        this reference from the dictionary later. If it overwrote a
        previously existing word, that word is still removed from the
        dictionary.
        '''
        if len(cls.mro()) > 2:
            _WordTracker.add_word(cls,name)
        super(_WordTracker, cls).__init__(name, bases, clsdict)
        
    @classmethod
    def add_word(cls,wordcls,name=None):
        '''
        Adds a word to the dictionary, either by name or by the name of 
        the class
        '''
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
        '''
        This function modifies the class to a specific word type.
        '''
        cls._class_word_type = wordtype
        return cls    
    return modifyWordTypeTo
        
class Word:
    '''
    The Word class, subclassing this adds it to the dictionary
    '''
    _class_word_type = UNDEFINED
    '''
    This defines the word type of this class. In Word it is undefined,
    in subclasses it is changed by the @WordType(..) decorator

    
    '''
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
        self.properties = {}


    def __getitem__(self,key):
        '''
        Gets the property (key) of the word
        '''
        return self.properties.get(key)

    def __setitem__(self,key,value):
        '''
        Sets the property (key) of the word
        '''
        self.properties[key] = value
    
    #This is where the word is evaluated to read data to
    #build the Action object
    def evaluate(self,action,sentence_iterator):
        '''
        Should evaluate the word, so that a complete idea is presented
        when an Action is made from a sentence
        (E.G. Sentence 'Create class "Foo"' would evaluate Create and then
        class would read in the next word "Foo" as the class name)
        
        Intended to be overwritten by subclasses, but provides default
        behavior.
        '''
        if(self.word_type() == VERB):
            action.predicate = self
        elif(self.word_type() == UNDEFINED):
            pass #Might want to change this to throw an error
        elif(self.word_type() == NOUN):
            action.direct_object = self
            if(not sentence_iterator.end() and \
               sentence_iterator.peek().word_type() == CDWORD):
                self["name"] = sentence_iterator.pop().to_str()
                #give direct object this name and pop it                
                pass
        elif(self.word_type() == ADVERB):

            if action.predicate != None:
                action.predicate[self.__class__.__name__] = True
            elif ( not sentence_iterator.end() and \
            sentence_iterator.peek().word_type() == VERB):
                verb = sentence_iterator.pop()
                verb.evaluate(action,sentence_iterator)
                verb[self.__class__.__name__] = True
                
            pass #Adverbs might want to overload this themselves
        elif(self.word_type() == ADJECTIVE):
            if(sentence_iterator.peek().word_type() == NOUN):
                word = sentence_iterator.pop()
                word.evaluate(action,sentence_iterator)
                word[self.__class__.__name__] = True
        else:
            pass #CDWORD, CDATA

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
    '''
    Regular expression that identifies a string as being only one word
    '''
    name_regex = re.compile("^(\"\w\S*\"|\'\w\S*\')$")
    '''
    Regular expression that identifies, in addition to only being one word,
    it is a valid class/variable name.
    '''
    def to_str(self):
        '''
        Modifies to_str to return the character data information rather
        than the class name.
        '''
        return self.str;
