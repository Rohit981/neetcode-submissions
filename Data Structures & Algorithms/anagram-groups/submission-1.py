class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list) # hashset for groupAnagrams

           #We loop through the list of strings
        for s in strs:
            count = [0]*26 #it will be 26 index array as we know it will have a to z characters

            #We loop through each and every string value
            for c in s:
                #Fill up the count array
                count[ord(c) - ord("a")] +=1
            hashset[tuple(count)].append(s)

        return list(hashset.values())
