from ..grammar import Word,WordType,NOUN
from .. import abstract

'''
This module simply contains a list of nouns we'll likely need.
'''

@WordType(NOUN)
class Class (Word):
    '''
    The noun "class".
    '''
#    def __init__(self):
#        super(self.__class__,self).__init__(NOUN)
    
    def create(self,**options):
        '''
        Creates a abstract.Class object, calls create on it.
        '''
        class_obj = abstract.Class(self["name"],options.get("in_location"))
        class_obj.create()

@WordType(NOUN)
class Function (Word):
    
    def create(self,**options):
        '''
        Creates a function. Requires that a class location be specified
        '''
        if(options.get("in") == None):
            raise Exception(
                "You need to specify where the function is defined")
        print("Created function %s in class \"%s\"" %
              (self["name"], options.get("in")))

    def define(self,**options):
        '''
        Synonym for create.
        '''
        self.create(**options)

if  "__main__" == __name__:
    a = Class();
    print(a.word_type())
    b = Function()
    print(b.word_type())
    print(b._word_type)
