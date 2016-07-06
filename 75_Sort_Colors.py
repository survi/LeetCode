class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n0 = 0
        n1 = 0 
        n2 = 0
        for i in range(len(nums)):
            # print 'nums[',i,']:',nums[i],
            k10 = n1 > n0
            k21 = n2 > n1
            if nums[i] == 0:
                nums[n0] = 0


                if k10:

                    nums[n1] = 1
                    n0 = n0 + 1
                    n1 = n1 + 1
                else:
                    n0 = n0 + 1
                    n1 = n0
                if k21:

                    nums[i] = 2
                    n2 = n2 + 1
                else:
                    n2 = n1



            elif nums[i] == 1:

                nums[n1] = 1


                if k21:

                    nums[i] = 2
                    n1 = n1 + 1
                    n2 = n2 + 1
                else:
                    n1 = n1 + 1
                    n2 = n1
            elif nums[i] == 2:
                nums[i] = 2
                n2 = n2 + 1

            # print 'n0:', n0, 'n1:', n1, 'n2:', n2,'nums:',nums



