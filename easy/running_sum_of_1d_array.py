class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        constant = 0 
        new_list = [ constant:=constant+x for x in nums ] 
        return new_list
