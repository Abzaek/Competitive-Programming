import numpy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lookup = defaultdict(int)
        nums.sort()
        ans = []
        subset = []
        def backtrack(index):

            if index >= len(nums):
                if tuple(subset) not in lookup:
                    ans.append(subset.copy())
                    lookup[tuple(subset)] += 1
                return
            
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            backtrack(index + 1)
        backtrack(0)
        return ans
            

        