# Implementation of Merge Sort
def merge(left_subarray, right_subarray):
    
    sorted_array = []

    left_subarray_copy = left_subarray.copy()
    right_subarray_copy = right_subarray.copy()

    left_subarray_deleted = 0
    right_subarray_deleted = 0

    right_subarray_pointer = 0
    left_subarray_pointer = 0

    for left_subarray_index in range(0, len(left_subarray_copy)):

        if( left_subarray_pointer > len(left_subarray_copy) - 1 or right_subarray_pointer > len(right_subarray_copy)-1 ):
            break 

        if(right_subarray_copy[right_subarray_pointer] < left_subarray_copy[left_subarray_pointer]):
            sorted_array.append(right_subarray_copy[right_subarray_pointer])
            del right_subarray[right_subarray_pointer-right_subarray_deleted]
            right_subarray_deleted += 1
            right_subarray_pointer += 1


            
        elif (right_subarray_copy[right_subarray_pointer] > left_subarray_copy[left_subarray_pointer]):
            sorted_array.append(left_subarray_copy[left_subarray_pointer])
            del left_subarray[left_subarray_pointer-left_subarray_deleted]
            left_subarray_deleted += 1
            left_subarray_pointer += 1

        elif (right_subarray_copy[right_subarray_pointer] == left_subarray_copy[left_subarray_pointer]):
            sorted_array.append(right_subarray_copy[right_subarray_pointer])
            sorted_array.append(left_subarray_copy[left_subarray_pointer])
            
            del left_subarray[left_subarray_pointer-left_subarray_deleted]
            del right_subarray[right_subarray_pointer-right_subarray_deleted]

            right_subarray_deleted += 1
            left_subarray_deleted += 1

            right_subarray_pointer += 1
            left_subarray_pointer += 1


    if(len(right_subarray) > 0):
        
        for y in right_subarray:
            sorted_array.append(y)

    elif (len(left_subarray) > 0):
        
        for y in left_subarray:
            sorted_array.append(y)

    
    return sorted_array
            
import math 

def mergeSort(p, r, listToBeSorted=[]):
    print(p, r)

    if (len(listToBeSorted) == 0):
        return listToBeSorted
    
    if p >= r:
        return [listToBeSorted[p]]
    
    q = math.floor((p+r)/2) 
    
    left_subarray = mergeSort(p, q, listToBeSorted)
    right_subarray = mergeSort(q+1, r, listToBeSorted)


    return merge(left_subarray, right_subarray)

def sort(listToBeSorted=[]):

    return mergeSort(0, len(listToBeSorted)-1, listToBeSorted)
