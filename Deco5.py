from functools import wraps
def Only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all ([type(arg) == int for arg in args]):
            return function(*args,*kwargs)
        print("Invalid")
        # data_list = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args,**kwargs)
        # else:
        #     print("Invalid argument")
    return wrapper  
@only_int_allow
def add_all(*args):
    total = 0 
    for i in args:
         total += i
    return total

print(add_all(1,2,3,4,[4,5,6,]))