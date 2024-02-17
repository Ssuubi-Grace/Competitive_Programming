class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        
        for op in operations:
            nums[nums.index(op[0])] = op[1]
        return nums

        
