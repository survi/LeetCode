class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        i = 0
        j = 0
        while i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i >= len(s):
                    return True
                else:
                    if j >= len(t):
                        return False
            else:
                j += 1
                if j >= len(t):
                    return False
        