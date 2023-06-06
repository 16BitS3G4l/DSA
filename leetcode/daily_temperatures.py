class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        results = [0 for x in range(0, len(temperatures))]

        stack = []
        total = 0
        
        for temp in range(0, len(temperatures)):
            
            if len(stack) != 0:
                last_element = stack[-1]
            
            while len(stack) > 0 and last_element[1] < temperatures[temp]:
                
                index = last_element[0]
                distance = temp-index 

                results[index] = distance 

                stack.pop()

                if len(stack) > 0:
                    last_element = stack[-1]


            stack.append( (temp, temperatures[temp] ) )
            
        return results