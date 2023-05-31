from linked_list import Node
from collections import OrderedDict

class LRUCache:

    def __init__(self, cache_size=4):
        self.elements = OrderedDict()
        self.linked_elements = Node("FIRST!")
        self.cache_size = cache_size

    def changeCacheSize(self, cache_size):
        self.cache_size = cache_size 


    def cacheMiss(self, dataRequested):
        prev_node = None

        # evict least recently used cache member
        if len(self.elements) == self.cache_size:
            last_cache_entry = next(reversed(self.elements.keys()))
            
            prev_node = self.elements[last_cache_entry].getPrev()

            if prev_node is not None:
                prev_node.changeNext(None)

            del self.elements[last_cache_entry] 


        temp_node = Node(dataRequested, self.linked_elements)

        self.linked_elements.setPrev(temp_node)

        self.elements[dataRequested] = temp_node
        self.elements.move_to_end(dataRequested, last=False)

        self.linked_elements = temp_node

        return self.linked_elements
    

    def cacheHit(self, dataRequested, hit):        
        
        del self.elements[dataRequested]

        # cache hit
        tempNode = Node(dataRequested, self.linked_elements)
                
        self.elements[dataRequested] = tempNode

        self.elements.move_to_end(dataRequested, last=False)

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