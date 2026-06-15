class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Intialize left and right pointer at the start and end of array
        left = 0
        right = len(numbers) - 1
        output = []

        while left < right:
            #Calculate the current sum
            current_sum = numbers[left] + numbers[right]

            #Check if current_sum is less than the target
            if current_sum < target:
                left+=1
            #Check if the sum == target if so then return the left index and right index value
            elif current_sum == target:
                output.append(left+1)
                output.append(right+1)
                return output
            else:
                right-=1
       
        