class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return -1
        fdict = {}
        for i in range(0,len(s)):
            if fdict.get(s[i], True) == False:
                continue
            if len(s.split(s[i])) >2:
                fdict[s[i]] = False
            else:
                return i
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l <= 0:
            return -1
        fdict = {}
        for i in range(0,len(s)):
            if fdict.get(s[i], True) == False:
                continue
            elif len(s.replace(s[i], "")) < l-1:
                fdict[s[i]] = False
            else:
                return i
        return -1