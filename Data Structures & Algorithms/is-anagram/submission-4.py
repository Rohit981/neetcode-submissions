class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #Optimal Approach
        #Create 2 hasmaps for s and t
        hashmap_s, hashmap_t = {}, {}

        #As the len of s and t will be same we will loop through s and check the indices
        for i in range(len(s)):
            #Add to hashmap
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i],0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i],0)
        
        #Loop through the hashmap to check if the elements are equal
        for count in hashmap_s:
            if hashmap_s[count] != hashmap_t.get(count,0):
                return False
        return True



        
