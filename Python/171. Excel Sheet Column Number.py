class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ndict = {}
        for i in range(1,27):
            ndict[chr(i+64)] = i
        row = 0
        l = len(s)-1
        for si in s:
            row += ndict[si]*(26**l)
            l -= 1
        return row