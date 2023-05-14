class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        
        # first attempt: combine hashmap with merge sort for O(n log n + n + k)
        # where k is the number of the elements with highest frequency to return 

        # idea: accomplish this better than n log n complexity
        
        number_frequencies = {

        }

        for num in nums:
            
            if number_frequencies.get(num) is None:
                number_frequencies[num] = 1
            else:
                number_frequencies[num] += 1
        
        k_positions = [[] for x in range(0, len(nums))]

        for number in number_frequencies.keys():
            
            number_frequency = number_frequencies.get(number)


            k_positions[number_frequency-1].append(number)

        
        top_k_frequent = []
        top_k_processed = 0

        for y in range(len(k_positions)-1, -1, -1):

            if(len(top_k_frequent) == k):
                return top_k_frequent 

            if len(k_positions[y]) > 0:
                
                for number in k_positions[y]:
                    
                    if(top_k_processed == k):
                        return top_k_frequent

                    top_k_frequent.append(number)
                    top_k_processed += 1

        # print(top_k_frequent)

        return top_k_frequent
        # reverse 

