class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

DP is used as base, redict records all the already computed result for future use, and maxsqrt define the max square root can be tried next time.


class Solution(object):
    count2beat = None
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count2beat = n
        if n <= 0:
            return 0
        self.minSquare(n, 0, n, {})
        return self.count2beat
            
    def minSquare(self, n, countnow, maxsqrt, redict):
        if countnow < self.count2beat:
            nsqrt = math.sqrt(n)
            if redict.get(n, False):
                self.count2beat = min(countnow + redict[n], self.count2beat)
                return redict[n]
            if nsqrt == int(nsqrt):
                self.count2beat = min(countnow + 1, self.count2beat)
                return 1
            tempcount = n
            k = min(maxsqrt, nsqrt)
            for i in range(int(k),0,-1):
                m = n - int(i)**2
                tempcount = min(tempcount, 1 + self.minSquare(m, countnow + 1, i, redict))
            redict[n] = tempcount
            return tempcount
        else:
            return n
        