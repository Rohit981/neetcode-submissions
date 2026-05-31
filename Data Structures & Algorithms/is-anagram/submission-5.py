class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #Optimal Approach
        #Create 2 hasmaps for s and t
        hashmap_s, hashmap_t = {}, {}

        #As the len of s and t will be same we will loop through s and check the indices
        for char_s,char_t in zip(s,t):
            #Add to hashmap
            hashmap_s[char_s] = 1 + hashmap_s.get(char_s,0)
            hashmap_t[char_t] = 1 + hashmap_t.get(char_t,0)
        
        #Loop through the hashmap to check if the elements are equal
        for count in hashmap_s:
            if hashmap_s[count] != hashmap_t.get(count,0):
                return False
        return True



        
