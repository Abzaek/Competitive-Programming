class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        initiate max_len, r, l, flag

        '''

        max_len = 0
        l = 0
        r = 0
        s = set()

        while r < len(nums):
            if nums[r] == 0:
                if 0 not in s:
                    s.add(0)
                else:
                    while nums[l] not in s:
                         l += 1
                    l += 1

            max_len = max(max_len, r - l)
            r += 1
        return max_len
            
