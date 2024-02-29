class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lookup = defaultdict(int)

        def backtrack(arr):
            nonlocal nums
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in lookup:
                    lookup[nums[i]] += 1
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.pop()
                    del lookup[nums[i]]
        backtrack([])
        return ans

        