class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        s = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                s = (j-i)*height[i] if (j-i)*height[i] > s else s
                i += 1
            else:
                s = (j-i)*height[j] if (j-i)*height[j] > s else s
                j -= 1
                
        return s
                
        