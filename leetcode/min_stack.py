class MinStack(object):

    def __init__(self):
        self.elements = []
        self.minimum_elements = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
         # compare previous minimum and current value
        
        
        if len(self.minimum_elements) == 0:
            current_min = float("inf")
        else:
            current_min = self.minimum_elements[-1]

        
        self.minimum_elements.append(min(val, current_min))
        self.elements.append(val)


    def pop(self):
        """
        :rtype: None
        """

        val = self.elements.pop()
        self.minimum_elements.pop()

        return val 
        

    def top(self):
        """
        :rtype: int
        """
        return self.elements[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum_elements[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646, 2147483646, 2147483647)

print(param_4)