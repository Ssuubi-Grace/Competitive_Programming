class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less,equal,more=[],[],[]        
        for i in nums:
            if i<pivot:
                less.append(i)
            if i>pivot:
                more.append(i)
            if i==pivot:
                equal.append(i)
        new_Arr=less+equal+more  
        return new_Arr     

