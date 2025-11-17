import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
variable = input("what ")
for item in movies["genres"]:
    if item == variable:
        print(movies["title"])