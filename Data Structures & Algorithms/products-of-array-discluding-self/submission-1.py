class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            #First create an empty output array
            output = []

            #Calculate the length of nums
            n = len(nums)

            #Initialize left and right product as 1 for mathimatical calculation
            left_product = [1]*n
            right_product = [1]*n

            #Loop through the left side of the nums and exclude the first element as it will be blank
            for l in range(1,n):
                left_product[l] = left_product[l-1]*nums[l-1]
            
            #Loop through the right side of the nums from backwards and exclude the last element as it will be blank
            for r in range(n-2,-1,-1):
                right_product[r] = right_product[r+1]*nums[r+1]
            
            #Calculate the output by multiplying the left and right side product
            for i in range(n):
                output.append(left_product[i]*right_product[i])
            
            return output



           