class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nd = {}
        print nd.get(1,0)
        for n in nums:
            if nd.get(n,0) == 0:
                nd[n] = 1
            elif nd.get(n,0) == 1:
                nd.pop(n)
        return nd.keys()[0]

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return reduce(lambda x,y:x^y, nums)