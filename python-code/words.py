import word
class Class (word.Word):
    def __init(self):
        Word("noun")
        
    def create(self,name,**options):
        print("Created class \"%s\"!" % name)
        if(options.get("in_location") != None):
            print("It was in %s" % options.get("in_location"))

a = Class()
a.create("Baka!", in_location = "your face")
