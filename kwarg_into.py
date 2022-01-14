# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")

# func(first_name = "Govind", Last_name = "Sharma")

def func(name, *args, Last_name = 'unknown', **kwargs ):
    print(name)
    print(args)
    print(Last_name)
    print(kwargs)

func('Govind',1,2,3, a = 1,b = 4)
