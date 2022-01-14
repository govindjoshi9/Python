name = ['abc','abcde', 'govind']

# for pos, name in enumerate(name):
#     print(f"{pos}---->{name}")
def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1
print(find_pos(name,'govind'))

