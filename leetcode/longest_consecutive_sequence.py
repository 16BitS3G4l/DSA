class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        processed_nums = set(nums)

        max_sequence_length = 0 
        length = 0 
        
        for num_index in range(0, len(nums)):
            num = nums[num_index]

            if num in processed_nums and num-1 not in processed_nums:

                length = 1 

                sequence_exists = True 
                sequence_member = num + 1

                while sequence_exists:
                    
                    if sequence_member in processed_nums:
                        length += 1

                    else:
                        sequence_exists = False

                    sequence_member += 1
                
            
            if length > max_sequence_length:
                max_sequence_length = length

        return max_sequence_length
