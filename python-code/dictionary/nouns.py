import word
from word import Word,WordType,NOUN
import abstract

'''
This module simply contains a list of nouns.
'''
@WordType(NOUN)
class Class (word.Word):

#    def __init__(self):
#        super(self.__class__,self).__init__(NOUN)
    
    def create(self,**options):
        '''
        CREATES A CLASSE!!!!LOL
        '''
        class_obj = abstract.Class(options.get("name"),options.get("in_location"))
        class_obj.create()

@WordType(NOUN)
class Function (word.Word):
    
    def create(self,name,**options):
        if(options.get("in_location") == None):
            raise Exception(
                "You need to specify where the function is defined")
        print("Created function %s in class \"%s\"" %
              (name, options.get("in_location")))

    def define(self,name,**options):
        self.create(name,**options)

if  "__main__" == __name__:
    a = Class();
    print(a.word_type())
    b = Function()
    print(b.word_type())
    print(b._word_type)
