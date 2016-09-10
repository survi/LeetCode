class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n0 = dividend
        n1 = divisor
        ############################################
        # deal with negative situations
        if n0 == 0:
            return 0
        if n1 == 1:
nre = n0
if nre > 2147483647:
            nre = 2147483647
        elif re < -2147483648:
            nre = -2147483648
return nre
        neg = False
        if n0 > 0 and n1 < 0:
            n1 = 0 - n1
            neg = True
        elif n0 < 0 and n1 > 0:
            n0 = 0 - n0
            neg = True
        elif n0 < 0 and n1 < 0:
            n0 = 0 - n0
            n1 = 0 - n1
        
        ############################################
        # do the binary division
        m0 = bin(n0)[2:]
        i = 0
        headm = ''
        re = ''
        while i < len(m0):
            tempm = headm + m0[i]
            if int(tempm,2) < n1:
                headm = tempm
                re = re + '0'
            else:
                tempm = bin(int(tempm,2) - n1)[2:]
                # print 'tempm = bin(int(tempm,2) - n1)[2:]:',tempm
                headm = tempm
                re = re + '1'
            i = i + 1
        ############################################
        # check if there is an overflow
        nre = int(re,2)
        if neg:
            nre = 0-nre
        if nre > 2147483647:
            nre = 2147483647
        elif re < -2147483648:
            nre = -2147483648
return nre



##very slow
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = 0
        m = ((dividend>0 and divisor<0) or (dividend<0 and divisor>0))
        dividend, divisor = abs(dividend), abs(divisor)
        # if divisor == 1:
        #     n = dividend
        ldd = len(str(dividend))
        lds = len(str(divisor))
        dl = ldd - lds
        re = 0
        while dl >= 0:
            tempds = divisor
            for i in range(dl):
                tempds = int(str(tempds) + '0')
            if dividend >= tempds:
                dividend -= tempds
                re += 1
            else:
                dl -= 1
                if dl >= 0:
                    re = int(str(re) + '0')
        if m:
            re = 0 - re
        if re > 2147483647:
            re = 2147483647
        elif re < -2147483648:
            re = -2147483648
        
        return re
        
        