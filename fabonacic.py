def fabonic(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabonic(n-1)+ fabonic(n-2)
number = int(input("Enter a no"))
print(fabonic(number))
