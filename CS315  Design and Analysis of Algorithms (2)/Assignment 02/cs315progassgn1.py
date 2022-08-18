import numpy as np
import time



# BubbleSort

def bubbleSort(numofelts):

    arr = np.random.randint(1000,size=(numofelts))
    start_time = time.time()
    n = len(arr)
    

    # Traverse through all array elements

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]

        if swapped == False:
            end_time = time.time()
            
            
    
    end_time = time.time()
    print("Bubble_Sort \t\t " + str(end_time-start_time))
    


# insertionSort

def insertionSort(numofelts):

    arr = np.random.randint(1000,size=(numofelts))
    start_time = time.time()
    n = len(arr)

    for i in range(1,n):
        key = arr[i]

        j = i-1

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
    end_time = time.time()
    print("Insertion_Sort \t\t " + str(end_time-start_time))

    return arr




# SelectionSort


def selectionSort(numofelts):

    arr = np.random.randint(1000,size=(numofelts))
    start_time = time.time()
    n = len(arr)

    for i in range(n-1):
        min_ind = i

        for j in range(i+1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
                arr[i],arr[min_ind] = arr[min_ind],arr[i]

                
    end_time = time.time()
    print("Selection_Sort \t\t " + str(end_time-start_time))

    return arr




# heapSort

def heapify(arr,n,i):

    # find largest among root and children

    largest = i

    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    # If root is not largest, swap with largest and continue heapifying
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(numofelts):

    arr = np.random.randint(1000,size=(numofelts))
    start_time = time.time()
    n = len(arr)

    # build max heap

    for i in range(n//2,-1,-1):
        heapify(arr,n,i)


    for i in range(n-1,0,-1):
        #swap
        arr[i],arr[0] = arr[0],arr[i]

        # heapify the root element
        heapify(arr,i,0)

    end_time = time.time()
    print("Heap_Sort \t\t " + str(end_time-start_time))
    return arr




# mergeSort
def mergeSortInit(numofelts):
    arr = list(np.random.randint(1000,size=(numofelts)))
    start_time = time.time()
    mergeSort(arr)
    end_time = time.time()
    print("Merge_Sort \t\t " + str(end_time-start_time))
    
    


def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1






# QuickSort

def quickSortInit(numofelts):
    arr = list(np.random.randint(1000,size=(numofelts)))
    size = len(arr)
    
    start_time = time.time()
    quickSort(arr, 0, size - 1)
    end_time = time.time()
    print("Quick_Sort \t\t " + str(end_time-start_time))


# function to perform quicksort
def quickSort(array, p, r):
    
    if p < r:
        
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        q = partition(array, p, r)
        # recursive call on the left of pivot
        quickSort(array, p, q - 1)
        # recursive call on the right of pivot
        quickSort(array, q + 1, r)


# function to find the partition position
def partition(array, p, r):
    
    # choose the rightmost element as pivot
    pivot = array[r]
    
    # pointer for greater element
    i = p - 1
    
    # traverse through all elements - compare each element with pivot
    for j in range(p, r):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

    
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

            
    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[r]) = (array[r], array[i + 1])

    
    # return the position from where partition is done
    return i + 1






def algorithmRunningTimeCalculator(numofelts):
    print("\n*************************************************************")
    print("Algorithmn \t\t Running_Time at " + str(numofelts) + " elements")
    bubbleSort(numofelts)
    insertionSort(numofelts)
    selectionSort(numofelts)
    heapSort(numofelts)
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    print("\n*************************************************************")

# for 100000 elements bubble,insertion and selection Sort takes a long time 

def algorithmRunningTimeCalculator_100000(numofelts):
    print("\n*************************************************************")
    print("Algorithmn \t\t Running_Time at " + str(numofelts) + " elements")
    heapSort(numofelts)
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    print("\n*************************************************************")


        
algorithmRunningTimeCalculator(10)
algorithmRunningTimeCalculator(100)
algorithmRunningTimeCalculator(1000)
algorithmRunningTimeCalculator(10000)
algorithmRunningTimeCalculator_100000(100000)     # Takes very long time for bubble,selection,insertion sorting algorithms



