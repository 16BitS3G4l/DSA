class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        counter_found = {}
        for x in nums:

            if counter_found.get(x) is not None:
                return True
            else: 
                counter_found[x] = 1
        
        return False 