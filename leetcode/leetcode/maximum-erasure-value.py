class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        initialize lookup, score, l, r
        '''

        l = 0
        r = 0

        score = 0
        max_score = score
        lookup = set()

        while r < len(nums):
            score += nums[r]
            if nums[r] not in lookup:
                lookup.add(nums[r])
            else:
                while True:
                    score -= nums[l]
                    lookup.remove(nums[l])
                    if nums[l] == nums[r]:
                        break
                    l += 1
                l += 1
                lookup.add(nums[r])

            max_score = max(score, max_score)
            r += 1

        return max_score
        