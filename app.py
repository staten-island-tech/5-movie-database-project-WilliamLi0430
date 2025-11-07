import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the entire movie list
data = json.load(movies)
print("What category are you searching up? ")
searchbar = input("Categories: title, year, cast, genres, href, extract, thumbnail, thumbnail_width, thumbnail_height. ")
for i in data:
    if searchbar.lower() in i["title"].lower():
        print(f"{i["title"].lower()} ")
    else:
        print(f"{i["title"].lower()} ")






#input("Categories: title, year, cast, genres, href, extract, thumbnail, thumbnail_width, thumbnail_height. ")
#for index, item in enumerate(data):
    #print(item["title"])