# 1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other
# def seq(n):
#     if len(n) == len(set(n)):
#         return True
#     else:
#         return False

# print(seq([2,3,4,5,6]))
# print(seq([2,3,4,5,5,6,7]))

# 2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))

# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
# def rem_lis(num_lis):
#     posti = 3-1
#     idx = 0
#     len_list = len(num_lis)
#     while len_list>0:
#         idx = (posti +idx)%len_list
#         print(num_lis.pop(idx))
#         len_list -= 1
# num = [10,20,30,40,50,60,70,80,90]
# rem_lis(num)

# 4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers
# number = []


# # 5. Write a Python program to create the combinations of 3 digit combo
# number = []
# for num in range(1000):
#     num = str(num)
# print(num)
# number.append(num)

# 6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.



def twoSum(self, nums, target):
        
        nums = [int(input(self))]
        target = int(nums.lenght())
        return target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
print(twoSum([1,2,3,4,5],3,4))
        
