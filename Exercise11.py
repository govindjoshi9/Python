def squae_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

# list, str
number = list(range(1,11))
print(squae_list(number))