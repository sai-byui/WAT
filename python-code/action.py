import sentence

'''
Basically, an evaluated sentence
'''

__author__ = "Brigham Young University - Idaho : Society for Artificial Intelligence"

class Action:
    predicate = Word() #Other names: Action, verb, ???
    direct_object = Word()
    context = {} #options for the action

    """
    Basically, a top-level verb in a sentence becomes the predicate,
    a top-level noun becomes the direct_object
    a top-level adverb becomes context?
    Just my thoughts, ~Logan
    """
    
    def __init__(sentence):
        #builds the action context
        #words are evaluated into how they affect the sentence
        #the predicate comes from the verb, chooses what is done
        #the direct_object word is where the method is called
        #The context comes from adverbs and such, they're like the
        #parameters of the action
        pass

    def perform(self):
        #use "action" to find the correct method of direct_object
        #call that method using the context provided
        pass
