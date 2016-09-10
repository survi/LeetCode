class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)< k:
            return 0
        maxl = 0
        return self.maxlength1(s, k, maxl)
        
    def maxlength1(self, s, k, maxl):
        print '--------------------------------'
        print 'len(s)', len(s)
        i = 0
        pool = set()
        countdict = {}
        while i < len(s):
            countdict[s[i]] = countdict.get(s[i], 0) + 1
            pool.add(s[i])
            if countdict[s[i]] >= k and i >= maxl:
                print 'i', i
                print 's[i]', s[i]
                thisone = True
                for p in pool:
                    thisone = thisone and countdict[p] >= k
                print thisone
                if thisone:
                    maxl = max(maxl,i+1)
            i += 1
        if maxl >= len(s):
            return maxl
        else:
            return self.maxlength1(s[1:], k, maxl)
                    
                
            
                
            
        