from heap import MaxHeap, HeapElement

class PriorityQueue:

    def __init__(self):
        self.elements = MaxHeap()
    
    def enqueue(self, val, priority):
        elem = HeapElement(val, priority)
        
        self.elements.insert(elem)
        
    def dequeue(self):
        self.elements.removeMax()
