class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        lookup = defaultdict(list)

        for i in range(len(nums)):
            lookup[nums[i]].append(i)

        ans = [None]*len(nums)

        def solve(key):
            arr = lookup[key]
            total = 0

            for i in range(1, len(arr)):
                total += arr[i] - arr[0]
            ans[arr[0]] = total

            for i in range(1, len(arr)):
                total -= (arr[i] - arr[i - 1])*(len(arr) - 1 - i)
                total += (arr[i] - arr[i - 1])*(i - 1)
                ans[arr[i]] = total
        for i in lookup.keys():
            solve(i)
        return ans
        


        