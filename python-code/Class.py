import os



class Class:
    def __init__(self, class_name, file_name = None):
        self.class_name = class_name
        if file_name == None:
            self.file_name = class_name
        else:
            self.file_name =file_name

        self.target = open(self.file_name, 'w+')




    def create(self,class_name, function_name):
        #top of file
        self.target.write('import os\n\n\n')
        #write the title of the class
        self.target.write('class %s:\n' % class_name)
        #default constructor
        self.target.write('\tdef __init__(self):\n')
        self.target.write('\t\tpass\n\n')
        self.target.write('\t def %s():' % function_name)






test = Class("test","test.py")

test.create("test", "hello_world")