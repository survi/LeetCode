class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            s = float(s)
            return True
        except:
            print s
            return False
            
        