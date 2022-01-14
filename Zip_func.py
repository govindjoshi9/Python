# user_id = ['user1','user2','user3']
# name = ['Govind', 'Nikita', 'Ujjwal']

# print(list(zip(user_id,name)))

# example = [('a',1), ('b',2)]
# print(dict(example))

# l = [(1,2), (3,4),(5,6),(7,8)]
# l1,l2 =list(zip(*l))
# print(l1)
# print(l2)

# def avg_finder(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
avg_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder([1,2,3],[4,5,6],[7,8,9]))
        
