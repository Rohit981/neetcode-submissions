class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #We will use hashset to get Time complexity of o(n) and space o(n)
       hashset = set()

       for n in nums:
            #First we check for duplicates if they exist then return true
            if n in hashset:
                return True
            hashset.add(n)
       return False

       

           
    
