class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        K, tot, curr, d = sum(nums)%p, len(nums), 0, {0:0}
        if K == 0:
            return 0
        for i,x in enumerate(nums):
            curr = (curr+x) % p
            if (curr-K) % p in d:
                tot = min(tot, i+1-d[(curr-K)%p])
            d[curr] = i+1
        return (tot if tot < len(nums) else -1)