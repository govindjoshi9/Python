# user_info = {
#     'name' : 'Govind',
#     'age' : 19,
#      'movies' : ['KGF','Tandav'],

# } 
# print(user_info['name'])
# if 'name' in user_info:
#     print("presant")
# else:
#     print("Not presant")
# if 'Govind' in user_info.values():
#     print("presant")
# else:
#     print("Not presant")

# for i in user_info.values():
#     print(i)

# user_info['fav_song'] = ['pachtoge']
# user_info
# print(user_info)

# d = {'name':'unknown', 'age': 'unknown' }
# d= dict.fromkeys("abc","unknown")
# d.clear()
# print(d)
# print(d.get('names', 'not found'))


def word_counter(s):
    count ={}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter("Govind"))