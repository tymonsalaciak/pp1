import json 
dic = {
    "country" : "poland",  
    "population" : 1000,
     "country" : "poland",  
    "population" : 1000,
     "country" : "poland",  
    "population" : 1000
}


in_fav = open("fav.json", "w")

json.dump(dic, in_fav, intend = "4")

in_fav.close()


