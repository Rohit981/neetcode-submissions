class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
                nums.sort()
                current_streak = 1
                longest_streak = 1

                #One edge case
                if len(nums) == 0 or len(nums) == 1:
                    return len(nums)
                
                for i in range(len(nums) - 1):
                    prev = nums[i]
                    current = nums[i+1]
                    print(prev, current)

                    if(current == prev + 1):
                            current_streak+=1
                            longest_streak = max(longest_streak,current_streak)
                    elif(current == prev):
                            continue
                    else:
                            current_streak = 1
                
                return longest_streak

            