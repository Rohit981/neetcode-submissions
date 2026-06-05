class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Variable for streaks
        current_streak = 0
        longest_streak = 1

        #Create a nums hash set
        num_set = set(nums)

        #Edge cases
        if len(nums) == 0 or len(nums) == 1:
                return len(nums)

        #loop through the set
        for num in num_set:
                #Check is num is not in the hashset to find the start and the end point
                if num-1 not in num_set:
                        current = num
                        current_streak = 1
                        #Check for while the current+1 is in the hashset
                        while current+1 in num_set:
                                current_streak+=1
                                longest_streak = max(longest_streak,current_streak)
                                current+=1
        return longest_streak
                
            