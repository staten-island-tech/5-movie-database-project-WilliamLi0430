import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
variable = int(input("what after"))
variables = int(input("what before"))
for index, item in enumerate(data):
    if item["year"] > variable and item["year"] < variables:
        print(item["title"])