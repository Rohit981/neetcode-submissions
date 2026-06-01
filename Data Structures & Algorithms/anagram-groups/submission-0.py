class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            if len(strs) <= 1:
                return [strs]
            
            hashset = defaultdict(list) #For anagram

            #Loop through the list to get the values
            for s in strs:
                count = [0]*26 #there are 26 lowercase letters

                for c in s:
                    count[ord(c) - ord("a")] += 1
                
                hashset[tuple(count)].append(s)
            return list(hashset.values())