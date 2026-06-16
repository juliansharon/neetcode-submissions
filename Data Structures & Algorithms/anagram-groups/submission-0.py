class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result_map = defaultdict(list)
        for i in range(len(strs)):
            final_result_map["".join(sorted(strs[i]))].append(strs[i])
        final_result = []
        for k,v in  final_result_map.items():
              final_result.append(v) 
        return final_result      

