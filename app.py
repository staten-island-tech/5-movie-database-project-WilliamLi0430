import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the entire movie list
data = json.load(movies)
searchbar = int(input("What"))
if int("year") > searchbar:
    print("title")






#input("Categories: title, year, cast, genres, href, extract, thumbnail, thumbnail_width, thumbnail_height. ")
#for index, item in enumerate(data):
    #print(item["title"])