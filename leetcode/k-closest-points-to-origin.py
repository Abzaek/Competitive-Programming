class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda a: a[0]**2 + a[1]**2)
        
        ans = [points[0]]
        pntr = 1

        while len(ans) < k and pntr < len(points):
            ans.append(points[pntr])
            pntr += 1

        return ans


        