class A:
    def mat(self):
        return "This is methos from class A"

class B(A):
    def mat(self):
        return "This is methos from class B"
    pass
class C(A):
    def mat(self):
        return "This is methos from class C"
    pass
class D(C,B):
    def mat(self):
        return "This is methos from class D"
    pass

a= A()
b = B()
c = C()
d = D()

print(d.mat())