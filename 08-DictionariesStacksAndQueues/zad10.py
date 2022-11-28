"""
10.	Create an array with 5 dictionaries, each containing a country and its population. 
Then, using ‘while’ loop, display the array contents.
"""

arr =[
    {"country" : "poland",  "population" : 1000},
    {"country" : "germany",  "population" : 1000},
    {"country" : "poland",  "population" : 1000},
    {"country" : "poland",  "population" : 1000},
    {"country" : "poland",  "population" : 1000},
]

print(arr[0])
print("-------------")


i = 0 
for i in arr:

#while i < len(arr):
    for key, value in i.items():
    #for key, value in arr[i].items():
         print(key, ":" , value)
    #print(arr[i]["country"])

     
    i += 1 

"""
x = True                                            jak nie kozystac z while
while x == True:
        print(arr)
        x = False
"""