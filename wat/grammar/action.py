from sentence import Sentence
from word import Word
'''
Basically, an evaluated sentence
'''

__author__ = "Brigham Young University - Idaho : Society for Artificial Intelligence"

class Action:

    """
    Basically, a top-level verb in a sentence becomes the predicate,
    a top-level noun becomes the direct_object
    a top-level adverb becomes context?
    Just my thoughts, ~Logan
    """
    
    def __init__(self,sentence):
        self.predicate = None #Other names: Action, verb, ???
        self.direct_object = None
        self.context = {} #options for the action
        
        iterator = sentence.iter()
        for word in iterator:
            word.evaluate(self,iterator)
        #builds the action context
        #words are evaluated into how they affect the sentence
        #the predicate comes from the verb, chooses what is done
        #the direct_object word is where the method is called
        #The context comes from adverbs and such, they're like the
        #parameters of the action
        pass

    def perform(self):
        if(self.direct_object != None and self.predicate != None):
            getattr(self.direct_object,self.predicate.to_str().lower())()
        #use "action" to find the correct method of direct_object
        #call that method using the context provided
        pass            
