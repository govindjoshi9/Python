# l = [1,2,3,4]
# # print(list(map(lambda a : a**2, l)))

# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

# print(my_map(lambda a : a**3 , l))

# def outer_func():
#     def inner_func():
#         print("inside inner func")
#     return inner_func()

# # var = outer_func()
# def outer_func2(msg):
#     def inner_func2():
#         print(f"message is {msg}")
#     return inner_func2

# var = outer_func2("hello there !")
# var()

# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# cube = to_power(3)
# print(cube(5))

def decorator_function(any_function):
    def wrapper_function():
        print('this is awasom function')
        any_function
    return wrapper_function

@decorator_function
def func1():
    print("This is function 1")

func1()

@decorator_function
def func2():
    print("this is function 2")

func2()

# var = decorator_function(func1())
# var()
# func1 = decorator_function(func1())
# func1()