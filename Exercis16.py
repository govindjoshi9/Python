user = {}

name = input("whats your name")
age = input("whats your age")
fav_movie = input("favieret movie")
fav_songs = input("favierat sons")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movie
user['fav_songs'] = fav_songs
for key, value in user.items():
    print(f"{key} : {value}")