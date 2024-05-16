class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        _count = len(points)
        
        points.sort(key = lambda x: x[0])
        right = points[0][1]

        for point in points[1:]:
            if point[0] <= right:
                _count -= 1
                right = min(right, point[1])
            else:
                right = max(right, point[1])
        return _count

        
        
        
        
        
        
        
        