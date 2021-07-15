user = {}

name = input("what is your name :")
age = input("what is your age :")
fav_movie = input("what is your favourite movie :").split(',')
fav_songs = input("what is your favourite songs :").split(',')

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_songs'] = fav_songs

for key, value in user.items():
    print(f"{key} : {value}")