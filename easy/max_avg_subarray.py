class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = -1000000
        i = 0      
        while( i+k <= len(nums)):
        
            avg = max(sum(nums[i:i+k]) / k  , avg) 
            i+=1
        return avg I
