import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = s.lower()

        if(len(s) == 0):
            return True

        j = 0
        for i in range(len(s)-1, -1, -1):
            
            if(s[i] != s[j]):
                return False
        
            j += 1

        return True