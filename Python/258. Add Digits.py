class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tmp = 0
            while num >= 10:
                tmp = num % 10 + tmp
                num = num / 10
            num = tmp + num
        return num


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tmp = 0
            for i in str(num):
                tmp = tmp + int(i)
            num = tmp
        return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 9 != 0:
            return num % 9  
        else:
            if num == 0:
                return 0
            else:
                return 9

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        dr = num - 9 * (abs(num - 1)/9)
        return dr

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            dr = num - 9 * ((num - 1)/9)
            return dr
