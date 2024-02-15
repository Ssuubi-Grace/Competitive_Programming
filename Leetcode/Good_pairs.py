class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        seen = {}

        for num in nums:
            if num in seen:
                count += seen[num]
                seen[num] += 1
            else:
                seen[num] = 1

        return count   
