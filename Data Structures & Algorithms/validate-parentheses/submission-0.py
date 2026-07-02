class Solution:
    def isValid(self, s: str) -> bool:
        #First create a dictionary of pairs
        pairs = {
            "}": "{",
            ")" : "(",
            "]" : "["
        }

        #Initilaize a stack
        stack = []

        #Loop through the values of String
        for char in s:
            if char not in pairs:
               stack.append(char)
            else:
                 #Check for top most element is equal to the pairs key value
                if not stack or stack[-1] != pairs[char]:
                    return False
                
                stack.pop()
                
        
        return not stack

        