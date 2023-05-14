# Implementation of Quick Sort

def quickSort(startIndex, lastIndex, listToBeSorted=[]):

    if startIndex >= lastIndex:
        return 
    
    pivot = lastIndex
    pointer = startIndex-1

    for y in range(startIndex, lastIndex+1):
        
        if(listToBeSorted[y] < listToBeSorted[pivot]):
            pointer += 1
            
            pointerValue = listToBeSorted[pointer]
            listToBeSorted[pointer] = listToBeSorted[y]
            listToBeSorted[y] = pointerValue

    pointer += 1
    pointerValue = listToBeSorted[pointer]
    listToBeSorted[pointer] = listToBeSorted[pivot]
    listToBeSorted[pivot] = pointerValue 

    quickSort(0, pointer-1, listToBeSorted)
    quickSort(pointer+1, lastIndex, listToBeSorted)


def sort(listToBeSorted=[]):
    quickSort(0, len(listToBeSorted)-1, listToBeSorted)
