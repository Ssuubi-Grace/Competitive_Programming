class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a, b = 0, int(c**0.5)  # Initializing pointers a and b
        while a <= b:
            total = a*a + b*b
            if total == c:
                return True
            elif total < c:
                a += 1
            else:
                b -= 1
        return False

