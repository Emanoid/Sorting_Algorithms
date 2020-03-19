#Quick Sort

def swap(a,b,lon):
    index_a = lon.index(a)
    index_b = lon.index(b)
    lon[index_a] = b
    lon[index_b] = a

def partition(low,high,lon):
    pivot = lon[low]
    pivot_index = low
    i = low + 1
    while i <= high:
        if lon[i] < pivot:
            swap(lon[i],lon[pivot_index],lon)
            pivot_index += 1
        i += 1
    swap(pivot,lon[pivot_index],lon)
    return pivot_index

def Quicksort(low,high,lon):
    if low < high:
        pivot_index = partition(low,high,lon)
        Quicksort(low,pivot_index,lon)
        Quicksort(pivot_index+1,high,lon)


l = [2,6,5,3,8,7,1,0]
Quicksort(0,len(l)-1,l)
print(l)

