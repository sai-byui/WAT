import os




class Class:
    def __init__(self, class_name, file_name = None):
        self.class_name = class_name
        # if no file name is passed, we are making a new file titled after the class
        if file_name == None:
            self.file_name = "%s.py" % class_name
            self.target = open(self.file_name, 'w+')
            self.is_new_file = True
        else:
            self.file_name = file_name
            self.target = open(self.file_name, 'a+')
            self.is_new_file = False



    def create(self):
        # give some spacing from any previous code
        if self.is_new_file == True:
            self.target.write('import os\n\n\n')
        else:
            # make some spacing
            self.target.write('\n\n\n')
        #write the title of the class
        self.target.write('class %s:\n' % self.class_name)
        #default constructor
        self.target.write('\tdef __init__(self):\n')
        self.target.write('\t\tpass\n\n')



test = Class("test")

test.create()