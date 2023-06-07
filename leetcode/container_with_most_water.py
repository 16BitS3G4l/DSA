class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxArea = 0
        
        right_pointer = len(height)-1
        left_pointer = 0 

        for i in range(0, len(height)):
            
            if right_pointer == left_pointer:
                break 

            distance = right_pointer - left_pointer
                    
            if height[left_pointer] > height[right_pointer]:
                    
                calculatedArea = distance * height[right_pointer]

                if calculatedArea > maxArea:
                    maxArea = calculatedArea

                right_pointer -= 1
            
            elif height[right_pointer] > height[left_pointer]:
                calculatedArea = distance * height[left_pointer]
                
                if calculatedArea > maxArea:
                    maxArea = calculatedArea

                left_pointer += 1

            else:
                calculatedArea = distance * height[left_pointer]

                if calculatedArea > maxArea:
                    maxArea = calculatedArea 

                left_pointer += 1

        return maxArea

