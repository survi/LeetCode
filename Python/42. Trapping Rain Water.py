# calculate the total area if rain drops are already filled up
# total area minus the area of the bars

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l<=2:
            return 0
        totalh = 0
        temph = height[0]
        maxh = height[0]
        maxpos = 0
        for i in range(1, l):
            if height[i] < maxh:
                temph += maxh
            else:
                maxh = height[i]
                maxpos = i
                totalh += temph
                temph = height[i]
        if maxpos < l-1:
            maxh = height[-1]
            temph = height[-1]
            for i in range(l-2,maxpos-1,-1):
                if height[i] < maxh:
                    temph += maxh
                else:
                    print i,maxh,maxpos,temph,
                    maxh = height[i]
                    totalh += temph
                    temph = height[i]
        totalh += height[maxpos]
        print totalh
        return totalh - sum(height)
                
                
                    
        