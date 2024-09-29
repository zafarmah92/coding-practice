class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash_set = set()
        l, res, best = 0, 0, 0
        for r in range(len(nums)):
            while nums[r] in hash_set:
                hash_set.remove(nums[l])
                res -= nums[l]
                l += 1 
            hash_set.add(nums[r])
            res += nums[r]
            best = max(res, best)

        return best

