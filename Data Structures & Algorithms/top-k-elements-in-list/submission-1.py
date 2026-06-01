class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a hashmap and ranks array
        frequency = {}
        ranks = [[] for n in range(len(nums) + 1)]

        #Create a frequency map
        for n in nums:
            frequency[n] = 1 + frequency.get(n,0)
        
        #Get the key and values of the map and append it to the rank array
        for key, value in frequency.items():
            ranks[value].append(key)
        
        res=[]
        #This is bucket sorting
        for i in range(len(ranks) - 1,0,-1):
            for n in ranks[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
       