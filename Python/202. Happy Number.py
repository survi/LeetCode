class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        recdict = {}
        while n != 1:
            if recdict.get(n,False) == False:
                recdict[n] = True
                n = self.calc2(n)
            else:
                return False
        return True
        
    def calc2(self, n):
        outre = 0
        for ni in str(n):
            outre += int(ni)*int(ni)
        return outre
