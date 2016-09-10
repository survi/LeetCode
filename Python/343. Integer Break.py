class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        k = n / 3
        m = n % 3
        if m == 1:
            return 4 * (3 ** (k-1))
        elif m == 2:
            return 2 * (3 ** k)
        else:
            return 3 ** k
        
        
        
        