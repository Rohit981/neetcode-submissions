class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                #Optimal Approach
                hashset = {}
                #Iterate through indices
                for i,n in enumerate(nums):
                        #Define a difference variable
                        dif = target - n

                        if dif in hashset:
                                return[hashset[dif], i]
                        
                        hashset[n] = i
            
