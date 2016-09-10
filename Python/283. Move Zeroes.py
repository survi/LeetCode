class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = []
        b = []
        for n in nums:
            if n == 0:
                b.append(n)
            else:
                a.append(n)
        nums[:]= a + b
        