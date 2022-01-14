# try:
#     age = int(input("Enter your age :"))
# except ValueError:
#     print("invalid inpute")

# if age<18:
#     print('you can not pay thos game')
# else:
#     print("ypu can play this game")


# try:
#     age = int(input("Enter your age :"))
# except ValueError:
#     print("invalid inpute")
# except:
#     print("unxepted error")

# else:
#     pass


# finally :
#     return finall block

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print("no must be enter")
# print(divide(10,"d"))
class NameTooShortErrror(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortErrror('name too short')

username = input("Enter your name")
validate(username)
print(f'hello{username}')