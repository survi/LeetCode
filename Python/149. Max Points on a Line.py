# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        linedict = {}
        outn = 0
        if len(points) == 1:
            return 1
        for i in range(len(points)):
            linedict = {}
            bonus = 0
            pmax = 0
            for j in range(i+1, len(points),1):
                tempa = None
                tempb = None
                
                tempa = (points[i].y - points[j].y) * 1.0/ (points[i].x - points[j].x) if points[i].x - points[j].x != 0 else 0
                tempb = points[i].y - points[i].x * tempa
                # print '===================================='
                # print i,':',j,':',
                # print tempa, tempb,
                if linedict.get(tempa, False) == False:
                    linedict[tempa] = {}
                if linedict[tempa].get(tempb, False) == False:
                    linedict[tempa][tempb] = 1
                linedict[tempa][tempb] += 1
                # print linedict[tempa][tempb],
                if points[i].y - points[j].y == 0 and points[i].x - points[j].x == 0:
                    bonus += 1
                    pmax += 1
                    pmax = max(pmax, linedict[tempa][tempb])
                else:
                    pmax = max(pmax, linedict[tempa][tempb] + bonus)
                # print pmax
            outn = max(pmax,outn)
        return outn
        
# [[1,2],[2,3],[2,4],[-1,4],[0,9],[3,4],[1,2],[2,3],[8,6],[5,6],[2,3]]
# [[3,1],[12,3],[3,1],[-6,-1]]