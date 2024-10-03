class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for n in nums:
            if n in _set:
                return True 
            _set.add(n)
        return False 
        """
        hash_set = dict()
        for i in nums:
            if i in hash_set:
                return True 
            else :
                hash_set[i] = 1
        return False
        """
