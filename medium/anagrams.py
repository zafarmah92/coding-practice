class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        return_set = defaultdict(list)

        for item in strs:
            count = [0] * 26
            for char in item:
                count[ord(char) - ord('a')] += 1 
            return_set[tuple(count)].append(item)
        
        return list(return_set.values())
