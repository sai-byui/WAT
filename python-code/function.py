import os



class Function:
    def __init__(self, function_name, file_name, class_name = None):
        # set function name
        self.function_name = function_name
        # set the file that we will insert the function into
        self.file_name = file_name
        # if there is no class, the function is not a method
        if class_name == None:
            self.is_method = False
        else:
            self.is_method = True

        # use append when we are adding to the file
        self.append = open(self.file_name, 'a+')


    def add_function(self):
        # if it is a method, pass different parameters. For now, it just passes the self parameter
        if self.is_method == True:
            self.append.write('\tdef %s(self):\n' % self.function_name)
            self.append.write('\t\tprint(\'Hello World\')\n')
        else:
            self.append.write('def %s():\n' % self.function_name)
            self.append.write('\tprint(\'Hello World\')\n')
        # algorithms and variables will be written here. For now it just prints hello world.


        # self.target.write('\t def %s():' % function_name)


t_function = Function("test_function", "test.py")

t_function.add_function()