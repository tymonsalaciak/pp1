import json

fav  = {
    "title" : "Pulp Fiction",
    "year" : 1994,
    "cast" : ["Tim Roth", "John Travolta", "etc"],
    "budget" : 50000,
    "director" : "Tarantino",
    "OST" : "perfect"
}

with open("favourite.json", "w") as in_json:
    json.dump(fav, in_json, indent=4)
