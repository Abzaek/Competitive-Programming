class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        prev = points[0]
        for i in points[1:]:
            count += self.distance(prev, i)
            prev = i
        return count

    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        maxmm = max(abs(x1 - x2), abs(y1 - y2))

        return maxmm

        


                
                
        