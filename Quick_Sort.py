#Quick Sort
'''
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
'''
##################################################################################
def partition(arr, l, h): 
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l, h): 
        if   arr[j] <= x: 
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 

# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def Quicksort(arr, l, h): 
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
    # initialize top of stack 
    top = -1
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    # Keep popping from stack while is not empty 
    while top >= 0: 
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

l = [2,6,5,3,8,7,1,0]
Quicksort(l,0,len(l)-1)
print(l)