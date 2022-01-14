# no1 = [2,4,6,8,10]
# no2 = [ 1,3,5,7,4,9]

# evens1 =[]
# for num in no1:
#     evens1.append(num%2==0)

# print(evens1)
# # print(all([True, True, True, True, True]))

# print(all([num%2==0 for num in no1]))
# print(any([num%2==0 for num in no2]))

# def my_sum(*args):
#     if all([(type(arg)== int or type(arg)== float) for arg in args ]): 
#         total =0
#         for num in args:
#             total += num
#         return total
#     else:
#         return "Wrong input"

# print(my_sum(1,2,3,4,3.4,23))