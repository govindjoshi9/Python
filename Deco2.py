from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print('this is awasom function')
        return any_function(*args,**kwargs)
    return wrapper_function


@decorator_function
def func(a):
    print(f"This is function with argument{a}")

# func(5)

@decorator_function
def add(a,b):
    return a+b

# print(add(2,5))
print(add.__doc__)
print(add.__name__)