class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            output = []

            for i in range(len(nums)):
                #To get right side elements
                right = nums[i + 1:]
                # print(f"Right Side: {right}")

                #Left side elements
                left = nums[:i]
                #    print(f"Left Side: {left}")

                product = 1
                for num in right:
                    product *=num
                
                for num in left:
                    product *=num
                
                output.append(product)
            
            return output
        