from ..grammar import Word, ADVERB, WordType

'''
This module is simply a list of adverb words
'''

@WordType(ADVERB)
class In(Word):
    '''
    Not yet implemented. Will need to overwrite the "evaluate method".
    Defines a location for an action to take place.
    
    Might need to be recursive, or a little bit complex for multiple uses.
    E.G., in sentences like "Create function 'doit' in package 'foo' in 
    module 'bar' in class 'Thing'".
    '''
    pass
#    def __init__(self):
#        super(self.__class__,self).__init__(ADVERB)
        
