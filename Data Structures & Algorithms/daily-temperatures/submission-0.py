class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Define a stack and results array
        results = [0] * len(temperatures)
        stack = []

        #Loop through all the temperatures index
        for current_index in range(len(temperatures)):
            #While the stack is present and current temp value is greater than the top of the stack
            while stack and temperatures[current_index] > temperatures[stack[-1]]:
                #Compute the previous index value
                previous_index = stack.pop()

                #Add the difference of current_index - previous_index to results
                results[previous_index] = current_index - previous_index
            
            #Push the current_index to the stack
            stack.append(current_index)
        return results
        