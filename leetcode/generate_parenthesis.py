class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 1:
            return ["()"]

        
        n_minus_one = self.generateParenthesis(n-1)

        results = []

        # if n == 4:
        #     results.append("( ( ) ) ( ( ) )")

        for a in n_minus_one:

            
            results.append("()" + a)
            
            if a + "()" != ("()" + a):
                results.append(a + "()")

            results.append("(" + a + ")")

    
        return results


a = Solution()
print(a.generateParenthesis(4))
# a = set(["(())(())","()()()()","(()()())","()(()())","(()())()","((()()))","()()(())","()(())()","(()(()))","()(())()","(())()()","((())())","()((()))","((()))()","(((())))"])
# b = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])


# print(b.difference(a))
# print(len(a))
# print(len(b))