import os
import Class

class File:
    def __init__(self, file_name, class_name = None):
        self.file_name = file_name
        if class_name == None:
            pass
        else:
            self.class_name = class_name

        self.target = open(self.file_name, 'w+')




    def create(self,file_name):
        #top of file
        self.target.write('import os\n\n\n')
        #write the title of the class
        self.target.write('# This is the %s file\n' % file_name)