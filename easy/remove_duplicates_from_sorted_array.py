class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted_nums = list(set(nums))
        sorted_nums.sort()
        for index, i in enumerate(sorted_nums):
            nums[index] = i
        if ( len(nums) - len(sorted_nums)) > 0 :
            nums[-( len(nums) - len(sorted_nums)):] = '_'
            for i in range(0,( len(nums) - len(sorted_nums))):
                nums.pop()
        else : 
            pass 
