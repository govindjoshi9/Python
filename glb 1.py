#

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
       # print("before calling rohan()",x)
        rohan()
        print("After  calling rohan()",x)
harry()
print(x)