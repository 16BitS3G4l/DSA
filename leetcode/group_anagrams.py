class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        results = {

        }

        for str in strs:
            count = [0 for x in range(0, 26)]

            for character in str:
                count[ord(character)-ord("a")] += 1

            if(results.get(tuple(count))) is None:
                results[tuple(count)] = [str]
            else:
                results[tuple(count)].append(str)

        return (list(results.values()))

v = Solution()
print(v.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))