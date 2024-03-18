class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        srtd = sorted(intervals)
        ans = []

        for interval in intervals:
            l = -1
            r = len(intervals) 
            while l + 1 < r:
                mid = l + (r - l)//2

                if srtd[mid][0] >= interval[1]:
                    r = mid
                else: 
                    l = mid
            ans.append(-1 if l == len(intervals) - 1 else srtd[r][-1])
        return ans

        