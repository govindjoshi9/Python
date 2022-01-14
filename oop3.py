class Employee:
    no_of_leaves = 9
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name},Salary is {self.salary}, and role is {self.role}"

harry = Employee("Harry", 876,"Programer")
rohan = Employee("rohan", 78, "student")

#arry.name = "Harry"
#harry.salary = 455
#harry.role = "Programmer"

#rohan.name = "rohan"
#ohan.salary = 455
#rohan.role = "student"

#print(rohan.printdetails())
print(harry.printdetails())