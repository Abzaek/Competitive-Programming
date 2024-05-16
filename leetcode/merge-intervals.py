class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 1
        ans = []
        intervals.sort()

        while r <= len(intervals):
            right_max = intervals[l][1]

            while r < len(intervals) and right_max >= intervals[r][0]:
                right_max = max(right_max, intervals[r][1])
                r += 1
            ans.append([intervals[l][0], right_max])
            l = r
            r += 1
        return ans

            

        