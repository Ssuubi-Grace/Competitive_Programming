class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        
        rev_s = words[::-1]
        
        result = ' '.join(rev_s)
        
        return result
        
