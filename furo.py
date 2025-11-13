import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
variable = int(input("what "))
for index, item in enumerate(data):
    if item["year"] == variable:
        print(item["title"])