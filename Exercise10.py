# def is_palindom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False

def is_palindom(word):
    return word == word[::-1]

print(is_palindom("naman"))
print(is_palindom("govind"))