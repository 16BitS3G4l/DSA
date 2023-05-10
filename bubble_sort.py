# Implementation of Bubble Sort
def sort(listToBeSorted=[]):

    # set to True so it passes at least once
    swapped = True
    
    while swapped:
        
        # reset swapped so it doesn't go on forever 
        swapped = False 

        for x in range(0, len(listToBeSorted)-1):
            
            if(listToBeSorted[x] > listToBeSorted[x+1]):
                
                tempX = listToBeSorted[x]
                listToBeSorted[x] = listToBeSorted[x+1]
                listToBeSorted[x+1] = tempX
                swapped = True

