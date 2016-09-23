class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        while len(s)>0:
            if len(s) != len(t):
                return False
            t = t.replace(s[0],'')
            s = s.replace(s[0],'')
            
        return True