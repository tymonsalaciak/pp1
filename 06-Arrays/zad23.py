"""
23.	Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. 
Define a function bubblesort(array) that returns the sorted array. Try to sort and display any three arrays.



def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            #jsśli zmienisz zank na < spowoduje to że posortuje malejąco 
            if arr[j] > arr[j+1]:
                change = arr[j]
                arr[j] = arr[j +1]
                arr[j+1] = change


arr1 =[4,-36,12,28,-9,-44,5,77]


print(bubblesort(arr1))

"""

def bubbleSort(array):
  for i in range(len(array)): # i 
    for j in range(0, len(array) - i - 1): #j - odpowiada za index w liscie 

      if array[j] > array[j + 1]:#[j + 1] dlatego że występuje przesunięcie pzoycji 

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


arr1 = [4,-36,12,28,-9,-44,5,77]

bubbleSort(arr1)

print('Sorted Array in Ascending Order:')
print(arr1)


