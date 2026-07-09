class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Define a stack
        stack = []
        #Define variable for area and max area
        area = 0
        max_area = 0

        #Iterate through the heights array
        for i,h in enumerate(heights):
            #Define the starting index variable
            start = i

            #We check for monostaticstack which will be keep computing untill the height is less than the top of the stack
            while stack and h < stack[-1][1]:
                #Pop the index and height
                index,height = stack.pop()
                #Compute the area and max area
                area = height * (i-index)
                max_area = max(max_area,area)
                start = index
            #Append the index value and the height as well
            stack.append([start, h])
        
        #Check for right boundary
        for index,height in stack:
            area = height*(len(heights) - index)
            max_area = max(max_area, area)

        return max_area

        