class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        difference_locator = {
            
        }

        position = 0 
        for num in nums:

            if difference_locator.get(target-num) is not None and difference_locator.get(target-num)[0] != position and num == target-num:
                difference_locator[target-num] = [difference_locator.get(target-num)[0], position]
                # pass

            else:
                difference_locator[target-num] = [position, -1] 

            position += 1


        # print(difference_locator)
        for entry in difference_locator.keys():
            
            if difference_locator.get(entry)[1] != -1 and difference_locator.get(entry)[0] != -1:
                return difference_locator.get(entry)
        
            if difference_locator.get(target-entry) is not None:
                
                if difference_locator.get(entry)[0] != difference_locator.get(target-entry)[0]:
                    return [difference_locator.get(entry)[0], difference_locator.get(target-entry)[0]]

        return list()
