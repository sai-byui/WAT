#   A
#  / \
# B   C
#  \ /
#   D
class A:
    def __init__(self):
        pass

class B(A):
    def b(self):
        pass

class C(A):
    def c(self):
        pass

class D(B,C):
    def d(self):
        pass
