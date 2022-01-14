# def total(a,b):
#      return a+b

# def all_total(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# # print(total(2,3,4))
# print(all_total(2,3,4))

def multiply_nums(*args):
    # print(num)
    print(args)
    multiplt = 1
    for i in args:
        multiplt *= i
    return multiplt
num = [2,3,4]
print(multiply_nums(*num))

