#E   A
# \ / \
#  B   C
#   \ /
#    D

class E:
    @staticmethod
    def out():
        print("Hi I'm E")

    def foo(self):
        print("E foo!")

class A:
    @staticmethod
    def out():
        print("Hi I'm A")

    def callFoo(self):
        self.foo()

    def foo(self):
        print ("A foo!")
    
    def __init__(self):
        pass
    
class B(E,A):
    def b(self):
        pass

class C(A):
    def c(self):
        pass

class D(B,C):
    def d(self):
        pass

A.out()
print("Heyo")
a =A()
a.out()
b = B()
b.out()
print("B Call foo!")

b.callFoo()
