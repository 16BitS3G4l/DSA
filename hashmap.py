# Implementation of a HashMap (String data types only) Data Structure 
class HashMap:

    def __init__(self, size=10):
        self.values = [0 for x in range(0, size)]
        self.size = size 
        print(self.values)

    # very simple hash function. This is not collision resistant at all, for demonstration purposes.
    def hash(self, key):
        return len(key)
    
    def put(self, key, value):
        index = self.hash(key)
        self.values.insert(index, value)

    def get(self, key):
        index = self.hash(key)
        return self.values[index]