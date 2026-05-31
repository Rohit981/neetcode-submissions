class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                #Optimal Approach
                hashset = {}

                #Iterate through indices
                for i in range(len(nums)):
                        #Define a difference variable
                        dif = target - nums[i]

                        if dif in hashset:
                                return[hashset[dif], i]
                        
                        hashset[nums[i]] = i
            
