import sentence

class Action:
    predicate = Word() #Other names: Action, verb, ???
    direct_object = Word()
    context = {}
    
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
