
# implementation of Linked List

class Node:

    
    def __init__(self, value, next=None):
        self.nextNode = next
        self.value = value 

    def changeNext(self, next):
        self.nextNode = next

    def changeValue(self, value):
        self.value = value


# implementation of Stack Data Structure Using Linked List

class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        temp = Node(value)

        temp.changeNext(self.head)
        self.head = temp


    def pop(self):
        temp = self.head 

        self.head = self.head.nextNode
        return temp.value 

# implementation of a Queue Data Structure Using a Linked List
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        
        temp = Node(value)

        temp.changeNext(self.head)

        if self.head == None:
            self.tail = temp

        self.head = temp 
        

    def dequeue(self):

        # the only situation in which they should be None is when there is absolutely no elements in the Queue
        if(self.head == None or self.tail == None): 
            return "No Elements Exist"

        nodeBeforeTail = self.head 
        tailNode = self.head 
        
        traversedCount = 0

        while tailNode.nextNode != None:
            traversedCount+=1
            nodeBeforeTail = tailNode    
            tailNode = tailNode.nextNode 
        
        
        prevTailValue = self.tail.value 
    
        if traversedCount == 0:
            self.head = None 
            self.tail = None 
        else:
            self.tail = nodeBeforeTail
            self.tail.changeNext(None)

        return prevTailValue
    


