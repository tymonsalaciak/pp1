"""
21.	Define a function compare(array1, array2) that returns True 
if both arrays are the same.  Arrays are the same if they have 
the same number of elements and values of elements in cells of 
arrays with the same index are equal. Then create a program and 
try to compare the following arrays: 

a.	["water","book","sky"]   ["water","book","sky"]
b.	[True,False]   [True,False,True]
c.	[5,3,1]   [5,3,1]
d.	[3,2,1]   [3,2]

Display both arrays and the result of comparison. Sample result:

Array1: water book sky
Array2: water book sky
Comparison: arrays are the same

        else:
            for i in arr1:
                print(i, end=" ")
                print(end="\n")
            for i in arr2:
                print(i, end=" ")
            print(end="\n")
            print("Comparison: arrays aren't the same")
  

"""
#w tym momęcie program wykonuje polecenie w całosci poprzez rozdzielenie pierwszego kluczowego warunku czy 
#obie tabliuce mają taką samą ilosc elementów jesli tak to czy te elementy są takie same 
#cały program byłby krótszy gdyby nie istrukvje print i specyfika ostatecznego wydruku


def compare(arr1,arr2):
    x = len(arr1)
    y = len(arr2)
    try:
        if x == y :
            if all(x in arr1 for x in arr2):
                for i in arr1:
                    print(i, end=" ")
                print(end="\n")
                for i in arr2:
                    print(i, end=" ")
                print(end="\n")
                print("Comparison: arrays are the same")
            else:
                for i in arr1:
                    print(i, end=" ")
                print(end="\n")
                for i in arr2:
                    print(i, end=" ")
                print(end="\n")
                print("Comparison: arrays aren't the same")   

    except:
        pass


compare(["water","book","sky"],["waterl","book","sky"])


#na ten momęt program liczy ich długość i osąda na tej podstawie 11:34 16.11.22