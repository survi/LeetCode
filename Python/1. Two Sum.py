class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[;]int]
        """
        ndict = {}
        for i in range(len(nums)):
            
            if ndict.get(target-nums[i], -1) > -1:
                return [ndict.get(target-nums[i], -1),i]
            else:
                ndict[nums[i]] = i
                
            
            
            
                
            
            
            

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try:
                re = nums.index(target-nums[i])
                if re != i:
                    return [i,re]
                else:
                    continue
            except:
                continue


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        minnum = min(nums)
        filteredlist = [ i for i in range(len(nums)) if nums[i] + minnum <= target]
        print filteredlist
        # filteredlist = nums
        for i in range(len(filteredlist)):
            for j in range(i+1,len(filteredlist),1):
                if (nums[filteredlist[i]] + nums[filteredlist[j]]) == target:
                    return [filteredlist[i],filteredlist[j]]
            




class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        minnum = min(nums)
        for i in range(len(nums)):
            if nums[i] + minnum > target:
                continue
            # print i
            for j in range(i+1,len(nums),1):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
            
            