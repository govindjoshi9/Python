class Employee:
    no_of_leaves = 9
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Programmer"

rohan.name = "rohan"
rohan.salary = 455
rohan.role = "student"

print(harry.no_of_leaves)
rohan.no_of_leaves = 8
print(Employee.no_of_leaves)
print(harry.__dict__)