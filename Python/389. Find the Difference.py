class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sdict = {}
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
        for i in range(len(t)):
            sdict[t[i]] = sdict.get(t[i], 0) - 1
            if sdict[t[i]] < 0:
                return t[i]