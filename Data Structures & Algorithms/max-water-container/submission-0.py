class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Using a two pointer approach intialize left and right pointer
        left = 0
        right = len(heights) - 1
        #Max area value
        max_area = 0

        #Check until the right value is greater than left
        while left < right :
            #Calculate the width and height of containers
            w = right - left
            h = min(heights[left], heights[right])

            #Calculate the area and max area
            area = w*h
            max_area = max(max_area,area)

            #Move the left pointer if the height of right is bigger or else move right pointer
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
                
        return max_area