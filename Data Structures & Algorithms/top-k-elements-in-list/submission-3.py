class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank = {}
        result = []
        for n in nums:
            rank[n]=rank.get(n,0)+1
        print(rank.items())    
        sorted_map = sorted( rank.items(), key = lambda x : x[1], reverse = True)

        result = []
        for i in range(k):
            result.append(sorted_map[i][0])  
        return result    

        