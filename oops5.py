class Employee:
    no_of_leaves = 9
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name},Salary is {self.salary}, and role is {self.role}"

@classmethod
def change_leaves(cls, newleaves):
    cls.no_of_leaves = newleaves
@classmethod
def from_str(cls,string):
    #param = string.split("-")
    #print(param)
    #return cls(param[0],param[1],param[2])
    return cls(*string.split("-"))

class programer(Employee):
    def __init__(self,aname,asalary,arole,aleanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.leanguage = aleanguage

    def printprog(self):
        return f"The name is {self.name}, Salary is {self.salary}, and role is {self.role} and leanguage is {self.leanguage}"
    pass



harry = Employee("Harry", 876,"Programer")
rohan = Employee("rohan", 78, "student")

karan = programer("Karan ",677, "Programer", "Puthon")
print(karan.printprog())