class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True 
        elif len(s) == 1:
            return False
        

        brackets = []

        brackets.append(s[0])

        for x in range(1, len(s)):
            
            if len(brackets) == 0:
                most_recent = s[x-1]
            else:
                most_recent = brackets[-1]
            

            if most_recent == '(' and s[x] in [']', '}']:
                return False
            if most_recent == '{' and s[x] in [']', ')']:
                return False
            if most_recent == '[' and s[x] in [')', '}']:
                return False
            
            if most_recent == '(' and s[x] == ')':
                brackets.pop()
                continue

            if most_recent == '{' and s[x] == '}':
                brackets.pop()
                continue

            if most_recent == '[' and s[x] == ']':
                brackets.pop()
                continue

            brackets.append(s[x])
            

        print(brackets)    
        if len(brackets) == 0:
            return True 
        else:
            return False
