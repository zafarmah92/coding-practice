class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_dict = {}
        map_dict[0] = -1
        count, max_len = 0, 0
        for num_index, number in enumerate(nums):
            if number == 1:
                count += 1
            else:
                count -= 1
            if count not in map_dict:
                map_dict[count] = num_index
            else:
                max_len = max((num_index - map_dict[count]), max_len)
        return max_len

