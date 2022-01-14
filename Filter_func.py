def is_even(a):
    return a%2 ==0

no = [3,4,5,6,7,82,1,3,43,33,44,]
even = tuple(filter(lambda a : a%2==0,no))
print(even)