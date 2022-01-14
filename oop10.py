class A:
    classvar1 = "I am in a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Construvtor"
        self.classvar1 = "Instance var in clas A"
        self.spacial = "Spacial"

class B(A):
     classvar1  = "I am in class B"

     def __init__(self):

         self.var1 = "I am inside class B's Construvtor"
         self.classvar1 = "Instance var in clas B"
         super().__init__()

a= A()
b = B()
print(b.spacial,b.var1, b.classvar1)