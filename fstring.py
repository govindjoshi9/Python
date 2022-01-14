# f string
import math
me = "Harry"
al = 3
#a = "This is %s %s"%(me,al)
#a= "This is {1} {0}"
#b = a.format(me,al)
a = f"this is {me} {al} {math.cos(90)}"
print(a)