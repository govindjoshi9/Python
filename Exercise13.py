def str_list(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element
word = ['abc', 'tuv', 'xyz']
print(str_list(word))