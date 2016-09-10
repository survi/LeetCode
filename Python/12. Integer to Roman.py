class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numlist = [
                    {'name':'M', 'value':1000, 'remain_name':'CM', 'remain_value':900},
                    {'name':'D', 'value':500, 'remain_name':'CD', 'remain_value':400},
                    {'name':'C', 'value':100, 'remain_name':'XC', 'remain_value':90},
                    {'name':'L', 'value':50, 'remain_name':'XL', 'remain_value':40},
                    {'name':'X', 'value':10, 'remain_name':'IX', 'remain_value':9},
                    {'name':'V', 'value':5, 'remain_name':'IV', 'remain_value':4},
                    {'name':'I', 'value':1, 'remain_name':'I', 'remain_value':1},
                ]
        outs = ""
        for (i,n) in enumerate(numlist):
            outs += n['name'] * (num/n['value'])
            num = num % n['value']
            if num >= n['remain_value']:
                outs += n['remain_name']
                num -= n['remain_value']
            
            
        return outs