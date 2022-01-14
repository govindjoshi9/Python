no = [1,2,3,4]

def square(a):
    return a**2

squares = list(map(lambda a: a**2,no))
print(squares)

squares_new = [i**2 for i in no]
print(squares_new)