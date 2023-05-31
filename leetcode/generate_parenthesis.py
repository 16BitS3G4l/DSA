class Solution(object):

    def generateSolutions(self, n, solution, open=0, closed=0):
        print(solution)

        if open == n and closed == n:
            return [solution]
        
        # the only way forward is to add a closing parentheses (since we used all our opens) 
        elif open == n and closed != n:
    
            return self.generateSolutions(n, solution + ")", open, closed+1)
        
        elif closed < open:

            adding_close = self.generateSolutions(n, solution+")", open, closed+1)
            adding_open = self.generateSolutions(n, solution+"(", open+1, closed)

            combined = []

            combined.extend(adding_close)
            combined.extend(adding_open)

            return combined 
    
        elif closed == open and (closed != n and open != n):
            return self.generateSolutions(n, solution + "(", open+1, closed)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        return self.generateSolutions(n, "(", 1, 0)