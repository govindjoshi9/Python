def func():
    global x
    x = 7
    return x

# def func2():
#     print(x)
x=5

print(func())
print(x)