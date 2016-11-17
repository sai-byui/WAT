from ..grammar import Word,VERB,WordType

'''
This modules contains a bunch of verbs
'''

@WordType(VERB)
class Create(Word):
    '''
    Creates different objects:
    *Classes
    *Functions
    +Files
    +Modules
    +Directories
    +Variables
    +Packages
    ???
    '''
    pass

@WordType(VERB)
class Define:
    '''
    Basically a synonym for create
    '''
    
    #    def __init__(self):
#        super(self.__class__,self).__init__(VERB);
