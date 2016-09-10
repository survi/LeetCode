class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        outint = (s.count('M')*1000 - s.count('CM')*200
            + s.count('D')*500 - s.count('CD')*200
            + s.count('C')*100 - s.count('XC')*20
            + s.count('L')*50 - s.count('XL')*20
            + s.count('X')*10 - s.count('IX')*2
            + s.count('V')*5 - s.count('IV')*2
             +s.count('I')*1)
        return outint
                

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numlist = [
                {'name':'M', 'value':1000},
                {'name':'CM', 'value':900},
                {'name':'D', 'value':500},
                {'name':'CD', 'value':400},
                {'name':'C', 'value':100},
                {'name':'XC', 'value':90},
                {'name':'L', 'value':50},
                {'name':'XL', 'value':40},
                {'name':'X', 'value':10},
                {'name':'IX', 'value':9},
                {'name':'V', 'value':5},
                {'name':'IV', 'value':4},
                {'name':'I', 'value':1},
                ]
        # print s.count("X")
        i = 0
        outint = 0
        for n in numlist:
            l = len(n['name']) - 1
            while i < len(s) and s[i:i+l+1] == n['name']:
                outint += n['value']
                i += 1 + l
                # if i >= len(s):
                #     break
        return outint
                