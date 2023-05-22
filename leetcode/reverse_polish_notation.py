class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        expressions = []
        values = []

        for token in tokens:
            
            # operator
            if token in ["+", "-", "/", "*"]:
                op = values.pop()
                op2 = values.pop()

                if token == '+':
                    values.append(int(op) + int(op2))
                elif token == '-':
                    values.append(int(op2) - int(op))
                elif token == '*':
                    values.append(int(op) * int(op2))
                elif token == '/':
                    values.append(int(op2) / int(op))
                
            else:
                values.append(token)


        return int(values[0])
    