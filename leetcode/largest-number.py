class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(x, y):
            if str(x) + str(y) > str(y) + str(x):
                return -1
            else:
                return 1
        
        ans = sorted(nums, key=cmp_to_key(comparator))

        if ans[0] == 0:
            return '0'

        return ''.join(map(str, ans))