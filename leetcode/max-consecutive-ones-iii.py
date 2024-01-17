class Solution:
    from collections import defaultdict
    def longestOnes(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        l = 0
        cSum = 0
        mSum = float('-inf')

        for i in range(len(nums)):
            hashMap[nums[i]] += 1
            if hashMap[0] <= k:
                cSum = hashMap[0] + hashMap[1]
            
            while hashMap[0] > k:
                hashMap[nums[l]] -= 1
                l += 1
            mSum = max(mSum, cSum)

        return mSum



        