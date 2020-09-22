# MRO - method resolution order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num=1

class D(B, C):
    pass


c = C()

print(D.num)
D.__str__