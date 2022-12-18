
import json

with open("students16.json", "r",encoding="utf-8") as fjson:
    content = json.load(fjson)

copy = []
for i, row in enumerate(content):
    copy.append({})
    for key, val in row.items() :
        if key != "id" and key != "fname" and key != "lname":
            continue
        else:
            copy[i][key] = val

with open("16.json","w",encoding="utf-8") as fjson:
    json.dump(copy,fjson,indent=4,ensure_ascii=False)

print("--------------------------------------")

with open("students16.json", "r",encoding="utf-8") as f:
    data = json.load(f)

result=[]
for i,row in enumerate(data):
    result.append({})
    for key,value in row.items():
        if key !="Id" and key!="Nazwa_produktu" and key!="Nazwa_producenta":
            continue
        else:
            result[i][key]=value

with open("1611.json","w",encoding="utf-8") as f:
    json.dump(result,f,indent=4,ensure_ascii=False)















        



"""
    with open("limited.json", "w") as limited:
        limit = json.load(fjson)
        
        for i in limit:
            copy = json.dumps(  i["fname"], i["lname"],i["id"],)
                json.dumps(lim["fname"], lim["lname"], lim["id"])


    with open("zad16.json", "w", encoding="utf-8") as ifjson:
        limit = json.load(fjson)
        object =  []
        for  i in limit["fname"].items(): 
            object.append(i)
 

        json.dump(object, limited, indent=4,)


"""          