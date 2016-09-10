class Solution(object):
    import random
    nums_original = []
    
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums_original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums_original
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        l = len(self.nums_original)
        templ = self.nums_original[:]
        re = []
        
        # test = []
        # i = 0
        # while i < 100:
        #     test.append(random.randrange(0,l,1))
        #     i += 1
        # print test
        # print collections.Counter(test)
        while l > 1:
            n = random.randrange(0,l,1)
            # n = int(random.random()*l)
            # print 'n:',n,'|templ[',n,']:',templ[n],
            re.append(templ[n])
            templ.pop(n)
            # print '|templ:',templ,
            l -= 1
            # print '|l:',l,
            if l == 1:
                re.append(templ[0])
                # print ''
                break
            # print '|re:',re
        return re
        


import random
class Solution(object):
    def __init__(self, nums):
        self.nums_original = nums
    def reset(self):
        return self.nums_original
    def shuffle(self):
        templ, l, re = self.nums_original[:], len(self.nums_original), []
        while l > 1:
            re.append(templ.pop(random.randrange(0,l,1)))
            l -= 1
            if l == 1:
                re.append(templ[0])
        return re
        
import random
class Solution(object):
    def __init__(self, nums):
    self.nums_original = nums

    def reset(self):
        return self.nums_original
        
    def shuffle(self):
        templ, l= self.nums_original[:], len(self.nums_original)
        for i in range(0,l,1):
            j = random.randrange(i,l,1)
            templ[i], templ[j] = templ[j], templ[i]
        return templ
        
import random
class Solution(object):
    def __init__(self, nums):
        self.reset = lambda : nums
        self.shuffle = lambda: random.sample(nums, len(nums))
