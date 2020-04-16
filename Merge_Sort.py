#Merge Sort

def mergesort(lon):
    return merge(lon,0,len(lon)-1)

def merge(lon,first,last):
    if first < last:
        middle = (first+last)//2
        merge(lon,first,middle)
        merge(lon,middle+1,last)
        return merger(lon,first,middle,last)

def merger(lon,first,mid,last):
    left = lon[first:mid+1]
    right = lon[mid+1:last+1]
    left.append(9999999999)
    right.append(9999999999)
    i = j = 0
    for k in range(first,last+1):
        if left[i] <= right[j]:
            lon[k] = left[i]
            i += 1
        else:
            lon[k] = right[j]
            j += 1
    return lon

'''
l = [2,8,5,3,9,4,1,7,4,23]
#print(l)
print(mergesort(l))
'''
##############################################################################

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0      
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
print(myList)
mergeSort(myList)
print(myList)