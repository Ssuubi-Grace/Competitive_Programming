class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        mixed = []
        for i in range(len(positive)):
            mixed.append(positive[i])
            mixed.append(negatives[i])
        return mixed
