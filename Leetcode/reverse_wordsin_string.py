class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        
        rev = words[::-1]
        
        result = ' '.join(rev)
        
        return result
        
