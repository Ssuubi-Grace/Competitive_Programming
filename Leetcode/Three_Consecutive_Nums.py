class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []
        mid_value = num // 3
        return [mid_value - 1, mid_value, mid_value + 1]      
        
