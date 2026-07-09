class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Create a tupile of position and speed, intantiate stack
        car_data = sorted(list(zip(position,speed)))
        stack = []

        #Loop through all the values in the car_data in reverse
        for p,s in reversed(car_data):
            #Calculate the current time
            time = (target-p)/s

            #Check if it's not a stack or time > top of stack values
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)