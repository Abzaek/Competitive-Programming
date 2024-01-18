class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}

        for i, item in enumerate(nums):
            if item in lookup:
                if i - lookup[item] <= k:
                    return True
                else:
                    lookup[item] = i
            else:
                lookup[item] = i
        return False
        