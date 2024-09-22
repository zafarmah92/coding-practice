class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        ## edge_case 
        prefix_sum[0] = 1 
        result_sum = 0 
        rolling_sum = 0
        for i in nums:
            rolling_sum += i

            if (rolling_sum - k) in prefix_sum:
                result_sum += prefix_sum[(rolling_sum - k)]

            if rolling_sum in prefix_sum:
                prefix_sum[rolling_sum] += 1
            else:
                prefix_sum[rolling_sum] = 1
                
        return result_sum 
