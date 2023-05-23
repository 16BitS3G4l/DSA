class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer_i = 0
        pointer_j = len(numbers)-1

        for n1 in range(0, len(numbers)):

            if numbers[pointer_i] + numbers[pointer_j] > target:
                pointer_j -= 1
                continue 

            if numbers[pointer_i] + numbers[pointer_j] < target:
                pointer_i += 1
                continue

            elif numbers[pointer_i] + numbers[pointer_j] == target:
                return [pointer_i+1, pointer_j+1]



