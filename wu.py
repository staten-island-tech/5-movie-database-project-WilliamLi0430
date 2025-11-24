import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

variable = input("what ")
for movie in data:
    for item in movie["title"]:
        if variable in item:
            print(movie["title"])