# implement max heap in Python
def indexExists(index, list):
    return 0 <= index <= len(list) -1


class HeapElement:

    def __init__(self, data, priority):
        self.val = priority
        self.data = data 
    
    def getData(self):
        return self.data 

    def setVal(self, val):
        self.val = val 

    def getVal(self):
        return self.val 

    def __eq__(self, other):
        return self.getVal() == other.getVal() 
    
    def __ge__(self, other):
        return self.getVal() >= other.getVal()

    def __gt__(self, other):
        return self.getVal() > other.getVal()
        
    def __lt__(self, other):
        return self.getVal() < other.getVal()
        

class MaxHeap:


    def __init__(self):
        self.elements = []

    
    def insert(self, val):
        self.elements.append(val)

        greater_than_parent = True

        while greater_than_parent:

            # check if parent even exists

            index = len(self.elements)-1
            parent_index = int ((index-1)/2)

            if self.elements[index] > self.elements[parent_index]:

                tempCurrent = self.elements[index]
                self.elements[index] = self.elements[parent_index]
                self.elements[parent_index] = tempCurrent

            else:
                greater_than_parent = False 



    def removeMax(self):
        self.elements[0] = self.elements[len(self.elements)-1]

        smaller_than_children = True  
        current_index = 0

        while smaller_than_children:
            right_child_index = 2 * current_index + 2
            left_child_index = 2 * current_index + 1
            
            if self.elements[left_child_index] > self.elements[right_child_index] and self.elements[current_index] < self.elements[left_child_index]:
                tempCurrent = self.elements[current_index]
                self.elements[current_index] = self.elements[left_child_index]
                self.elements[left_child_index] = tempCurrent

            elif self.elements[right_child_index] > self.elements[left_child_index] and self.elements[current_index] < self.elements[right_child_index]:
                tempCurrent = self.elements[current_index]
                self.elements[current_index] = self.elements[right_child_index]
                self.elements[right_child_index] = tempCurrent
            
            else:
                smaller_than_children = False 

            
        del self.elements[len(self.elements)-1] 

    def getMax(self):
        return self.elements[0]

    def heapify(self, list):

        for element in list:
            self.insert(element)
    
        return self.elements 
