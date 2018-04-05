class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.relist = []
        self.assign([],nums)
        return self.relist
        
    def assign(self, prenums, nums):
        if len(nums) <= 1:
            self.relist.append(prenums + nums)
        else:
            for i in range(len(nums)):
                self.assign(prenums+ [nums[i]],nums[:i]+nums[i+1:])
        