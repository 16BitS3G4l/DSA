def swap(list, firstIndexOfElementToSwap, secondIndexOfElementToSwap):
    tempSecondElementToSwap = list[secondIndexOfElementToSwap] 
    list[secondIndexOfElementToSwap] = list[firstIndexOfElementToSwap] 
    list[firstIndexOfElementToSwap] = tempSecondElementToSwap
    

# Implementation of Selection Sort
def sort(listToBeSorted=[]):
    
    for x in range(0, len(listToBeSorted)):
        
        minimumElementIndex = x 
        minimumElement = float("inf")

        for y in range(x, len(listToBeSorted)):
    
            if listToBeSorted[y] < minimumElement:
                minimumElementIndex = y 
                minimumElement = listToBeSorted[y]
        
        swap(listToBeSorted, x, minimumElementIndex)
    


