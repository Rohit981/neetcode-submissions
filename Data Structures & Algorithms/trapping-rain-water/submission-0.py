class Solution:
    def trap(self, height: List[int]) -> int:
        #Initialize variables left right and max left max right
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        water = 0
        current_water = 0

        #Two pointer approach
        while left < right:
            max_left = max(max_left,height[left])
            max_right = max(max_right, height[right])

            if max_left < max_right:
                left +=1
                max_left = max(max_left,height[left])
                current_water = max_left - height[left]
            else:
                right -=1
                max_right = max(max_right, height[right])
                current_water = max_right - height[right]
            
            water += current_water
        return water
