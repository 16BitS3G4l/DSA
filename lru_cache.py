from linked_list import Node

class LRUCache:

    def __init__(self, cache_size=4):
        self.elements = {}
        self.linked_elements = Node("FIRST!")


    def changeCacheSize(self, cache_size):
        self.cache_size = cache_size 


    def cacheMiss(self, dataRequested):
        prev_node = None

        # evict least recently used cache member
        if len(self.elements) == self.cache_size:
            last_cache_entry = next(reversed(self.elements.keys()))
            
            # node before the last node in the linked list 
            prev_node = self.elements[last_cache_entry].getPrev()

            if prev_node is not None:
                prev_node.setNext(None)

            del self.elements[last_cache_entry] 

        temp_node = Node(dataRequested, self.linked_elements)


        self.linked_elements.setPrev(temp_node)

        self.elements[dataRequested] = temp_node
        self.linked_elements = temp_node

        return self.linked_elements
    

    def cacheHit(self, dataRequested, hit):        
        
        # cache hit
        tempNode = Node(dataRequested, self.linked_elements)
        
        self.linked_elements.setPrev(tempNode)
        self.linked_elements = tempNode

        return self.linked_elements 


    def requestData(self, dataRequested):
        
        cache_query = self.elements.get(dataRequested) 

        # cache miss
        if cache_query is None:
            return self.cacheMiss(dataRequested)

        # cache hit       
        return self.cacheHit(dataRequested, cache_query) 

            
            


