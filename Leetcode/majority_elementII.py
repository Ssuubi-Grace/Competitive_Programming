class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        div = n // 3
        element = []
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
    
        for num, count in count_dict.items():
            if count > div:
                element.append(num)
    
        return element

