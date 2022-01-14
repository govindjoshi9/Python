# def revers_list(l):
#     l.reverse()
#     return l
# def revers_list(l):
#     return l[::-1]

def revers_list(l):
    r_list =[]
    for i in range(list(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list



number = [1,2,3,4]


print(revers_list(number))