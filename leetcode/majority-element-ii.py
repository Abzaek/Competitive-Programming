class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hshtbl = {}
        ans = []

        for i in nums:
            if i not in hshtbl:
                hshtbl[i] = 1
            else:
                hshtbl[i] += 1
        
        for i in hshtbl:
            if hshtbl[i] > len(nums)//3:
                ans.append(i)
        return ans

        