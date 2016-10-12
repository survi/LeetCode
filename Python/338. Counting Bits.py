class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        k = 4
        d = 4
        re = [0,1,1,2]
        if num <= 3:
            return re[:num+1]
        else:
            while k <= num:
                if k == 2*d:
                    d = k
                re.append(re[k-d]+1)
                k += 1
        return re