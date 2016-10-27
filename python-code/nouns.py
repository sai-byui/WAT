import word

class Class (word.Word):
    def __init(self):
        Word(word.NOUN)
        
    def create(self,name,**options):
        print("Created class \"%s\"!" % name)
        if(options.get("in_location") != None):
            print("It was in %s" % options.get("in_location"))

class Function (word.Word):

    def __init(self):
        Word(word.NOUN)

    def create(self,name,**options):
        if(options.get("in_location") == None):
            raise Exception(
                "You need to specify where the function is defined")
        print("Created function %s in class \"%s\"" %
              (name, options.get("in_location")))

    def define(self,name,**options):
        self.create(name,**options)
            
a = Class()
a.create("Baka!", in_location = "your face")
a = Function()
a.define("dance", in_location = "Baka!")
