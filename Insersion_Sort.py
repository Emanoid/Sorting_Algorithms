
def insertionSort(arr):
    for j in range(1, len(arr)): 
        key = arr[j] 
        i = j-1
        while i >=0 and key < arr[i] : 
            arr[i+1] = arr[i] 
            i -= 1
        arr[i+1] = key  

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)

