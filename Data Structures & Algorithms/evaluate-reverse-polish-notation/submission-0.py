class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Define a stack
        stack = []

        #Loop through the list of elements
        for token in tokens:
            #Check if token is a operator or not
            if token in {"+", "*", "-", "/"}:
                #pop the operators
                operand2 = stack.pop()
                operand1 = stack.pop()

                #Compute the result and push it
                if token == "+":
                    stack.append(operand2+operand1)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand2*operand1)
                elif token == "/":
                    stack.append(int(operand1/operand2))
            else:
                #Push the token
                stack.append(int(token))

        return stack[-1]
        