import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
variable = input("what ")
for index, item in enumerate(data):
    if item["title"] == variable:
        print(item["title"])