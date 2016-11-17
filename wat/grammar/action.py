from sentence import Sentence
from word import Word
'''
This module handles the evaluation of a Sentence object into an Action
object, which basically interprets the Word objects into a performable
action.

The actual ability of this action to be performed depends on the functions
of the individual word objects, and how Word.evaluate is implemented (though
it DOES have default behavior).
'''

__author__ = "Brigham Young University - Idaho : Society for Artificial Intelligence"

class Action:

    """
    This class is a container that reads in a Sentence object, evaluates it,
    and then can later perform the action by calling the perform method.
    
    What this will do is take the "direct_object" Word attribute, and then
    call the method on it that matches the predicate attribute's to_str()
    method (in lower case). (E.G., "Create class" will have a
    Class object as the direct object, and it will call 
    direct_object.create(**context)

    the **context is the context option passed as options to the create
    function. Words have the ability to modify this context if needed.
    """
    
    def __init__(self,sentence):
        '''
        Reads in the Sentence object, evaluating the different words. The
        Word.evaluate functions will modify this action object. After that,
        this Action object should be ready to perform()
        '''
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
        '''
        Performs the action, as it is understood by the Sentence.
        It does this by using the getattr function to get the function
        of direct_object with the name of the predicate, and then calling
        that function, passing in context as options.
        '''
        if(self.direct_object != None and self.predicate != None):
            getattr(self.direct_object,self.predicate.to_str().lower())(**self.context)
        #use "action" to find the correct method of direct_object
        #call that method using the context provided
        pass            
