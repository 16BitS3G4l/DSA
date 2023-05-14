class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        count = {

        }

        count2 = {

        }

        for letter_in_t in range(0, len(t)):
            
            if count.get(t[letter_in_t]) is not None:
                count[t[letter_in_t]] += 1
            else:
                count[t[letter_in_t]] = 1

            if count2.get(s[letter_in_t]) is not None:
                count2[s[letter_in_t]] += 1
            else:
                count2[s[letter_in_t]] = 1

        for tkey in count.keys():

            if count2.get(tkey) is None:
                return False
            elif count2.get(tkey) != count.get(tkey):
                return False
            
        return True
         