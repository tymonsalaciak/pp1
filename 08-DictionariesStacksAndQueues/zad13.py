import json

data = {}
data["keys"] = []
data["values"] = []
"""
for i in data["keys"]:
    for j in data["values"]:
"""      







while True:
    data["stuent"].append(input(f"give key and value separated with ( : )    :"))
    with open("student.json", "w") as in_json:
        json.dump(data , in_json, indent=4)

