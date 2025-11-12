import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])