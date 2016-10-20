class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        d = A[1] - A[0]
        startpos, outre = 0, 0
        for i in range(2,len(A)):
            if A[i] - A[i-1] == d:
                if i == len(A)-1:
                    outre += (i-startpos) * (i-startpos-1) / 2
            else:
                if i-startpos >= 3:
                    outre += (i-startpos-2) * (i-startpos-1) / 2
                startpos = i - 1
                d = A[i] - A[i-1]
        return outre