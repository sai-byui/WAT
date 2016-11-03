import word

'''
This module simply contains a list of nouns.
'''

class Class (word.Word):
    def __init__(self):
        super(self.__class__,self).__init__(word.NOUN)
        
    def create(self,name,**options):
        print("Created class \"%s\"!" % name)
        if(options.get("in_location") != None):
            print("It was in %s" % options.get("in_location"))

class Function (word.Word):

    def __init__(self):
        super(self.__class__,self).__init__(word.NOUN)
        
    def create(self,name,**options):
        if(options.get("in_location") == None):
            raise Exception(
                "You need to specify where the function is defined")
        print("Created function %s in class \"%s\"" %
              (name, options.get("in_location")))

    def define(self,name,**options):
        self.create(name,**options)
