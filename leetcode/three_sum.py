class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        triplets = []

        # O(n log n)
        nums.sort()
    
        used_numbers_as_fixed = {}

        for n1 in range(0, len(nums)):

            if used_numbers_as_fixed.get(nums[n1]) is not None:
                continue
            else:
                used_numbers_as_fixed[nums[n1]] = 1

            left_pointer = n1+1
            right_pointer = len(nums)-1

            used_numbers2_as_fixed = {}
            
            for n2 in range(n1+1, len(nums)):
                
                if left_pointer >= right_pointer:
                    break 
 
                summation = nums[left_pointer] + nums[right_pointer] + nums[n1]
                    
                if summation < 0:
                    left_pointer += 1
                    continue

                elif summation > 0:
                    right_pointer -= 1
                    continue

                triplets.append( [ nums[n1], nums[left_pointer], nums[right_pointer] ] )
                used_numbers2_as_fixed[nums[left_pointer]] = 1
                
                while left_pointer < right_pointer and used_numbers2_as_fixed.get(nums[left_pointer]) is not None:
                    left_pointer += 1

        return triplets
                
            
            


