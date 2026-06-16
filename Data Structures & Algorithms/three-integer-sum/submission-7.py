class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
    
        for i in range(n-1):
            # if nums[i]>0:
            #     break
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = n - 1
                    
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                target = 0

                if current_sum < target:
                    left+=1
                elif current_sum == target:
                        output.append([nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1    
                else:
                    right-=1

        return output 
            