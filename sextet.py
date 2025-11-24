import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

variable = input("what ")
for movie in data:
    for item in movie["genres"]:
        if item == variable:
            print(movie["title"])