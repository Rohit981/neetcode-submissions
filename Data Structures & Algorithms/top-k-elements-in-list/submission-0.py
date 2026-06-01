class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ranks = []
        
        for n in nums:
                frequency[n] = 1 + frequency.get(n,0)
                
        for key, value in frequency.items():
             ranks.append((key,value))
        
        ranks.sort(key=lambda x:x[1],reverse=True)
        
        result = [tup[0] for tup in ranks]
        return result[:k]
       