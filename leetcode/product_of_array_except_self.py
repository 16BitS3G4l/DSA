class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        prefix = [0 for x in range(0, len(nums))]
        postfix = [0 for x in range(0, len(nums))]
        output = []

        # populate prefix values 
        for num in range(0, len(nums)):   
            
            if num == 0:
                prefix[num] = 1
                continue
        
            prefix[num] = prefix[num-1]*nums[num]

        # populate postfix values 
        for num in range(len(nums)-1, -1, -1):   
            
            if num == len(nums)-1:
                postfix[num] = nums[num]
                continue
        
            postfix[num] = postfix[num+1]*nums[num]
        
        # calculate output
        output = [0 for x in range(0, len(nums))]
        for postfix_member in range(0, len(postfix)):

            if postfix_member == len(nums) - 1:
                output[postfix_member] = prefix[postfix_member-1]
            
            elif postfix_member == 0:
                output[postfix_member] = postfix[postfix_member+1]
            else:
                output[postfix_member] = prefix[postfix_member-1] * postfix[postfix_member+1]