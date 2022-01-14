# In this file we start learning about basic priactices of python
# import time
# print("Current date and time : \n",)
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# from math import pi
# r = float(input("Enter the radius :"))
# print("Area of the circle is " + str(r) + "is:" + str(pi * r**2))

# import datetime
# now = datetime.datetime.now()
# print("Current date and time :")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# a = (input("Enter the first name"))
# b = (input("Enter the Second name"))
# print("Hello",b, a)


# n = int(input("Enter the value of n"))
# nn = n*11
# nnn = n*111
# sum = 0
# sum = n + nn +nnn
# print(sum)

# a = int(input("Enter the value of a"))
# n = int("%s"%a)
# n2 = int("%s%s"% (a,a))
# n3 = int("%s%s%s"% (a,a,a))
# sum = n+n2+n3
# print(sum)

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[3])


# n = (input("Enter the value of n"))
# sp = n.split(".")
# print(sp[-1])

# val = (input("Enter the coma sprated value :"))
# list = val.split(",")
# tuple = tuple(list)
# print("List :", list)
# print("Tuple :", tuple)

# exam_st_date = (11, 12, 2014)
# print("The examination will start from : %i/%i/%i" % exam_st_date)

# r = int(input("Enter the radius of sphare"))
# pi =3.14
# vol = 4/3*pi*r**3
# print(vol)

# n = int(input("Enter the non negative integer"))
# cp = str(n.copyright(cp))
# print(cp)

# a b = int(input("Enter the 2nd no"))
# c = int(input("Enter the 3rd no"))
# sum = a= int(input("Enter the 1st no"))
# +b+c
# sum2 = 3*a+3*b+3*c
# if(a==b and b==c):
#     print(sum2)
# else:
#     print(sum)

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 

# print(abs.__doc__)

# Write a Python program to print the calendar of a given month and year.
# import calendar
# y = int(input('Enter the year'))
# m = int(input("Enter the month"))
# print(calendar.month(y,m))
    

# Write a Python program to print the following 'here document'.

# print("""a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example""")

# print("""I this line
# without any escape squence you
# do line......      change""")

# Write a python program to calucale no between two dates

# from datetime import date
# d1 = date(2002,4,9)
# d2 = date(2021, 7, 21)

# delte = d2-d1
# print(delte.days)

# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.


# def diff(n):
#         if n <= 17:
#                 return 17-n
                
#         else:
#                 return (n-17)*2

# print(diff(22))
# print(diff(14))

# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# def copy_String(str,n):
#         result = ""
#         for i in range(n):
#                 result = result + str
#         return result

# print(copy_String('abc',2))
# print(copy_String('.py',3))

# PRO 21 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user

# n = int(input('Enter the no:'))
# if n%2==0:
#         print('Even no')
# else:
#         print('odd no')
        
# 22. Write a Python program to count the number 4 in a given list.

# list = [1,2,43,4,5,3,4,6,5,4,4,4]

# print(list.count(4))

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 
# def cop_string(str, n):
#     fun = 2
#     if fun > len(str):
#         fun = len(str)
#     substr = str[:fun]
#     result = ''
#     for i in range(n):
#         result = result + substr
#     return result

# print(cop_string("abfefefe",3))
# print(cop_string("p",5))

# 24. Write a Python program to test whether a passed letter is a vowel or not.

# alp =  input('Enter the string :')
# if alp=='a' or alp == 'e' or alp== 'i' or alp == 'o' or alp == 'u':
#     print('Enterd word is vowel')
# else:
#     print('Entered word is consonent')

# 25. Write a Python program to check whether a specified value is contained in a group of values. 

# def serch(data,n):
#     for value in data:
#         if n == value:
#             return True
#     return False



# print(serch([1, 5, 8, 3],3))
# print(serch([1, 5, 8, 3],-1))

# 26. Write a Python program to create a histogram from a given list of integers

# def partten(item):
#     for n in item:
#         output = ''
#         times = n
#         while(times >0):
#             output += '@'
#             times = times -1
#         print(output)

# print(partten([2,3,4,6,5]))

# 27. Write a Python program to concatenate all elements in a list into a string and return it

# def concatenate_string(list):
#     result = ''
#     for i in list:
#         result += str(i)
#     return result
# print(concatenate_string([1,5,12,4]))

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence

# def printinf_even_no(list):
#     for elemant in list:
#         if(elemant%2==0):
#             print(elemant)
#         elif(elemant==237):
#             print(elemant)
#             break
# print(printinf_even_no([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527]))

# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))

#  Write a Python program that will accept the base and height of a triangle and compute the area

# def areaTriangle(b,h):

#     hy = b**2 + h**2
#     return hy**2 

# print(areaTriangle(20,40))

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers

# def gcd(n1,n2):
#     gcd = 1
#     if n1 % n2 ==0:
#         return n2
#     for k in range(int(n2/2),0,-1):
#         if n1 % k ==0 and n2 %k == 0:
#             gcd = k
#             break
#     return gcd

# print(gcd(12,17))
# print(gcd(4,6))
# print(gcd(336,360))

# Write a Python program to get the least common multiple (LCM) of two positive integers.
# def lcm(x,y):  
#     if x > y:
#         z = x
#     else:
#         z = y
#     while(True):
#         if((z % x == 0) and (z % y == 0)):
#             lcm = z
#             break
#         z +=1
#     return lcm

# print(lcm(4,6))
# print(lcm(15,17))


# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# def sumOfThree(n1,n2,n3):
    
#     sum = n1+n2+n3
#     if n1==n2 or n2==n3 or n3==n1:
#         sum = 0
#     return sum

# print(sumOfThree(2,3,4))
# print(sumOfThree(2,3,2))
# print(sumOfThree(3,3,3))

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# def sunTwo(n1,n2):

#     sum1 = n1+n2
#     if sum1 in range(15,20):
#         return 20
#     else:
#         return sum1

# print(sunTwo(15,2))
# print(sunTwo(5,8))
    


# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# def func(n1,n2):
#     if n1+n2 ==5 or n1-n2==5 or n1==n2:
#         return True
#     else:
#         return False

# print(func(3,2))
# print(func(7,2))
# print(func(2,2))

# 36. Write a Python program to add two objects if both objects are an integer type. 
# n1 = int(input("Enter the 1 integer :"))
# n2 = int(input("Enter the 2 integer :"))
# sum = int(n1+n2)
# print(sum)

# Write a Python program to display your details like name, age, address in three different lines. 

# name = input('Enter your name :')
# age = int(input('Enter your age :'))
# addres = input('Enter your addres :')

# print(f'your name is {name}\nyour age {age}\nyour adders {addres}')

# 38. Write a Python program to solve (x + y) * (x + y)

# def func(x,y):
#     return (x+y) * (x+y)

# print(func(4,3))

# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of year
# amt = 10000
# inr = 3.5
# t = 7
# futer_value = amt((1+(0.1*inr)**t))
# print(futer_value)

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# import math
# def distanc_func(x1,x2,y1,y2):
#     return math.sqrt(((x1-y1)**2)+((x2-y2)**2))

# print(distanc_func(4,0,6,6))

# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# import struct
# print(struct.calcsize('P')*8)

# 43. Write a Python program to get OS name, platform and release information
# import os
# import platform
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())

# 44. Write a Python program to locate Python site-packages
# import site
# print(site.getsitepackages())`

# 45. Write a python program to call an external command in Python.
# import psutil
# print(psutil.cpu_count())

# 46. Write a python program to get the path and name of the file that is currently executing.

# import os 
# print(os.path.realpath(__file__))

# 47. Write a Python program to find out the number of CPUs using

# import os
# print(os.cpu_count())

# 49. Write a Python program to list all files in a directory in Python. 
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/Documents/Python') if isfile(join('/Documents/Python', f))]
# print(files_list);

# 50. Write a Python program to print without newline or space

# for i in range(0,10):
#     print('*',end='')
# print('\n')

# 51. Write a Python program to determine profiling of Python programs
# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

# 52. Write a Python program to print to stderr.
# from __future__ import print_function
# from os import sep
# import sys
# def eprint(*args ,**kwargs):
#     print(*args, file=sys.stderr, **kwargs)

# eprint('abc','bcd','efc',sep='--')

# 53. Write a python program to access environment variables

# import os 
# print(os.environ)
# print(os.environ['HOME'])
# print(os.environ['PATH'])

# 54. Write a Python program to get the current username
# import getpass
# print(getpass.getuser())

# 55. Write a Python to find local IP addresses using Python's stdlib
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# 56. Write a Python program to get height and width of the console window.
# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())

# 57. Write a Python program to get execution time for a Python method.
# from os import times
# import time
# st = time.time()
# print(st)

# 58. Write a Python program to sum of the first n positive integers.
# def sumOfn(n):

#     n = (n*(n+1)/2)
#     return n
# print(sumOfn(8))

# 59. Write a Python program to convert height (in feet and inches) to centimeters

# feet = int(input('Enter the height in feet'))

# inch = feet*30.480
# print('Youer height in centimeter is ',inch)

# 60. Write a Python program to calculate the hypotenuse of a right angled triangle

# def tria(b,p):
#     import math
#     hyp= (b**2 +p**2)**0.5
#     return hyp
# print(tria(4,3))

# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles

# feet = int(input('Enter the distance in feet :'))

# inch = feet*12
# yeard = feet/3
# miles = feet/5,280
# print('Distance in inch ',inch)
# print('Distance in yeard ',yeard)
# print('Distance in miles ',miles)

# 62. Write a Python program to convert all units of time into seconds.

# hour = int(input('Enter the time in houres'))
# sec = hour*60*60
# print('Time in second is %i'% sec)

# 63. Write a Python program to get an absolute file path
# import os
# print(os.path.abspath('d1.py'))

# 64. Write a Python program to get file creation and modification date/times
# import os.path, time
# print('Creation time %s' % time.ctime(os.path.getctime('d1.py')))
# print("Modification time %s" % time.ctime(os.path.getatime('d1.py')))

# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

# sec = float(input('Enter the thime in sec :'))
# day = sec //(24*3600)
# sec %= (24*3600)
# hour = sec//3600
# sec %= 3600
# min = sec//60
# sec %= 60
# seco = sec

# print('The the currunt time is :%d/%d/%d/%d'% (day, hour, min,seco))

# 66. Write a Python program to calculate body mass index

# hig= float(input('Enter the highet in meeter :'))
# kg = float(input('Enter the wighte in kg :'))
# BMI = round(kg/(hig*hig),2)
# print('Your body mass index is ', BMI)

# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

# kip = float(input('Enter the pressuer in kilopascal'))
# pou= round(kip*0.145038,2)
# mmgh= round(kip*7.50062,3)
# atp= round(kip*0.00986923,3)
# print('Pressuer in pounds per square inch is :',pou)
# print('Pressuer in millimeter of mercury  is :',mmgh)
# print('Pressuer in atmoshperic pressuer  is :',atp)

# 68. Write a Python program to calculate the sum of the foure digits in an integer.
# num = int(input('Enter the four digit no :'))
# x = num//1000
# x1 = (num - x*1000)//100
# x2 = (num -x*1000 - x1*100)//10
# x3 = (num -x*1000 - x1*100 - x2*10)
# print('The sum of foure digit you enterd is :',x+x1+x2+x3)

# 69. Write a Python program to sort three integers without using conditional statements and loops. 
# a = int(input('Enter the first digit :'))
# b = int(input('Enter the second digit :'))
# c = int(input('Enter the third digit :'))

# a1 = min(a,b,c)
# c1 = max(a,b,c)
# b1 = (a+b+c)-a1-c1

# print('Sort of three no is :',a1,b1,c1)

# 70. Write a Python program to sort files by date.
# import glob
# import os 
# file = glob.glob('*.py')
# file.sort(key=os.path.getmtime)
# print('\n'.join(file))

# 72. Write a Python program to get the details of math module.

# import math
# print(dir(math))
# 73. Write a Python program to calculate midpoints of a line

# print('\nCalculating mid point of line :')
# x1 = float(input('\nEnter the x1 value :'))
# x2 = float(input('\nEnter the x2 value :'))
# y2 = float(input('\nEnter the y2 value :'))
# y1 = float(input('\nEnter the y1 value :'))

# mid_point = (((x1+x2)/2),((y1+y2)/2))
# print(mid_point)

# 75. Write a Python program to get the copyright information and write Copyright information in Python code.
# import sys
# print('\n printing a copyright sighn')
# print(sys.copyright)
# print(copyright)\

# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
# import sys
# print('The number of command line argumant of script :'),sys.argv[0]
# print('number of argumenr',len(sys.argv))
# print('Argument list :',str(sys.argv))

# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.

# import sys
# print()
# if sys.byteorder == 'Little':
#     print('little-endian system')
# else:
#     print('Big-endian system')
# print()

# 78. Write a Python program to find the available built-in modules.
# import sys
# print(sys.builtin_module_names)

# 79. Write a Python program to get the size of an object in bytes

# import sys
# from typing import Sized
# a = 23
# print(sys.getsizeof(a))

# 80. Write a Python program to get the current value of the recursion limit

# import sys
# print(sys.getrecursionlimit())
# 81. Write a Python program to concatenate N strings.
# l1 = ['Red', 'white', 'green']
# print('-'.join(l1))

# 82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)
# l1 = sum([10,20,30])
# l2 = sum({2,3,4})
# l2 = sum((1,2,3,4))
# print(l1,l2,l2)

# 83. Write a Python program to test whether all numbers of a list is greater than a certain number. 
# l1 = [5,6,7,8]
# print()
# print(all(x >1 for x in l1))
# print(all(x >5 for x in l1))

# 84. Write a Python program to count the number occurrence of a specific character in a string. 

# s = 'This is a spacific string to count a spacific character'
# print(s)
# print('"I" in string is\n')
# print(s.count('i'))

# 85. Write a Python program to check whether a file path is a file or a directory.
# import os
# path = 'd1.py'
# if os.path.isdir(path):
#     print('is directrory\n')
# elif os.path.isfile(path):
#     print("Its a normal file ")
# else:
#     print('Its a spacific path of file')

# 86. Write a Python program to get the ASCII value of a character/
# print('ASCII value of character')
# print(ord('a'))
# print(ord('A'))
# print(ord('1'))
# print(ord('@'))

# 87. Write a Python program to get the size of a file
# import os
# from typing import Sized
# print(os.path.getsize('d1.py'))

# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50"
# x=30
# y =20
# print('\n%d+%d=%d'%(x,y,x+y))

# 89. Write a Python program to perform an action if a condition is true. 
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

# n= 1
# if n==1:
#     print('First day of Month\n')
# else:
#     print()

# 90. Write a Python program to create a copy of its own source code
# 91. Write a Python program to swap two variables
# a = 34
# b = 45
# tamp = ''
# tamp = a
# a =b
# b = tamp
# print(a,b)

# 92. Write a Python program to define a string containing special characters in various forms
# 93. Write a Python program to get the Identity, Type, and Value of an object.
# a= 'govind'
# print(type(a))
# print(id(a))
# print(a)


# 94. Write a Python program to convert a byte string to a list of integers

# a = b'govind'
# print(list(a))

# 95. Write a Python program to check whether a string is numeric
# s = '2323'
# if type(s) == int:
#     print('Numaric type')
# else:
#     print('Normal string')

# 96. Write a Python program to print the current call stack
# import traceback
# print(traceback.print_stack)

# 96. Write a Python program to print the current call stack
# import modulefinder
# from types import ModuleType
# print(ModuleType)

# 98. Write a Python program to get the system time
# import time
# print(time.ctime())

# 99. Write a Python program to clear the screen or terminal.

# import os
# os.system('cls')

# 100. Write a Python program to get the name of the host on which the routine is running
# import socket
# print(socket.gethostname())

#103. Write a Python program to extract the filename from a given path
# 105. Write a Python program to get the users environmen
# import os 
# print(os.environ)

# 109. Write a Python program to check if a number is positive, negative or zero.

# n = int(input("Enter a no:"))
# if n==0:
#     print("Its a zero")
# elif n>0:
#     print("Positve no")
# else:
#     print('nagative no')

# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
# nl = [45,65,75,105,150,30,60]
# reslt = list(filter(lambda x : (x%15==0), nl ))
# print(reslt)

# 114. Write a Python program to filter the positive numbers from a list.
# nl = [45,65,75,105,150,7,11,23,30,60]
# res = list(filter(lambda x : (x%2==0),nl))
# print(res)

# 115. Write a Python program to compute the product of a list of integers (without using for loop)
# import math
# l1 =  [10,30]
# trd = math.prod(l1)
# print(trd)


