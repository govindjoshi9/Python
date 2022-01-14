from functools import wraps

def print_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper

@print_function
def add(a,b):
    return a+b
print(add(4,5))