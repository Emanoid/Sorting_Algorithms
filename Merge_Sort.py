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


l = [2,8,5,3,9,4,1,7,4,23]
#print(l)
print(mergesort(l))
