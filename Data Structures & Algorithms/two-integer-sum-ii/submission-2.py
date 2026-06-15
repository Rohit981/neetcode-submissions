class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        output = []

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum<target:
                left+=1
            elif sum == target:
                output.append(left+1)
                output.append(right+1)
                return output
            else:
                right-=1
        