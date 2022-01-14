def factorial_itrasiv(n):
    fac = 1
    for i in range(n):
        fac = fac * (i +1)
    return fac


def factorial_recarciv(n):
    if n == 1 :
        return 1
    else:
        return n * factorial_recarciv(n-1)

number = int(input("Enter a no"))
print("Factorial Using Itrasive Method",factorial_itrasiv(number))
print("Factorial Using recarcive  Method",factorial_recarciv(number))
