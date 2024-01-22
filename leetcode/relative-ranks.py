class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sor = sorted(score, reverse=True)
        lookup = {}
        for i, rank in enumerate(sor):
            if i > 2:
                lookup[rank] = str(i + 1)
            else:
                if i == 0:
                    lookup[rank] = 'Gold Medal'
                elif i == 1:
                    lookup[rank] = 'Silver Medal'
                else:
                    lookup[rank] = 'Bronze Medal'
        ans = []

        for i in score:
            ans.append(lookup[i])

        return ans
        