class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Create a left and right pointer
        left = 0
        right = len(s) - 1

        #Check if we have reached the middle
        while left < right:
            #Check if the left and right has alphanumeric value
            if s[left].isalnum() == False:
                left+=1
            elif s[right].isalnum() == False:
                right-=1
            else:
                #Compare left and right characters and if they are true then increament the value otherwise return False
                if s[left].lower() == s[right].lower():
                    left+=1
                    right-=1
                else:
                    return False
        return True
        