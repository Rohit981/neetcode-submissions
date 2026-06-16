class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #Initialize variables
        n = len(nums)
        output = []

        #Loop through the nums index and remove the left and right index
        for i in range(n -2):
            #Check for duplicates to avoid duplicate triplet
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            #Set left and right pointer
            left = i+1
            right = n-1

            #Loop through until right is greater than left
            while left < right:
                #Calculate the current sum
                current_sum = nums[i] + nums[left] + nums[right]
                target = 0

                #Check if the sum is less than target then move the left otherwise move right
                if current_sum < target:
                    left+=1
                elif current_sum == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1

                    #Check for left pointer duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    #Check for right pointer duplicate
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                else:
                    right-=1
        return output
        