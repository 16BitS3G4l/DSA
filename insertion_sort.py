def swap(list, firstIndexOfElementToSwap, secondIndexOfElementToSwap):
    tempSecondElementToSwap = list[secondIndexOfElementToSwap] 
    list[secondIndexOfElementToSwap] = list[firstIndexOfElementToSwap] 
    list[firstIndexOfElementToSwap] = tempSecondElementToSwap
    

# Implementation of Insertion Sort
def sort(listToBeSorted=[]):

    i = 0

    if(len(listToBeSorted) <= 1):
        return listToBeSorted 

    for x in range(1, len(listToBeSorted)):
        i += 1 

        for y in range(x-1, -1, -1):

            if(listToBeSorted[y] > listToBeSorted[y+1]):
                swap(listToBeSorted, y, y+1)
            else:
                break
    
    return listToBeSorted