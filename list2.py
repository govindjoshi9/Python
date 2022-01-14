no = list(range(1,21))
# no.pop()
# print(no.pop())
# print(no.index(4))
def nagative_list(l):
    nagative = []
    for i in l:
        nagative.append(-i)
    return nagative
print(nagative_list(no))