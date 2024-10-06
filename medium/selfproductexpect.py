class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = [1] * len(nums)
        prefix = 1
        suffix = 1 

        for i in range(len(nums)):
            return_list[i] *= prefix 
            prefix *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            return_list[i] *= suffix
            suffix *= nums[i] 

        
        return return_list
        
        
        """
        product_reference = defaultdict(list)
        for index,i in enumerate(nums):
            prefix_elements = tuple(sorted(nums[:index]))
            suffix_elements = tuple(sorted(nums[index+1:]))
            #print(f"prefix {nums[:index]}, element {nums[index]} suffix {nums[index+1:]}, {product_reference}")
            if prefix_elements not in product_reference:
                product_reference[prefix_elements] = math.prod(prefix_elements)
            if suffix_elements not in product_reference:
                product_reference[suffix_elements] = math.prod(suffix_elements)
            
            return_list.append(product_reference[prefix_elements]*product_reference[suffix_elements])
            #print(return_list)
        return return_list 
        """
