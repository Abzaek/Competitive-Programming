class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0]*len(nums)
        accumulator = 0
        nums.sort(reverse=True)
        _sum = 0

        for request in requests:
            if request[1] == len(nums) - 1:
                prefix_sum[request[0]] += 1
                continue

            prefix_sum[request[0]] += 1
            prefix_sum[request[1] + 1] -= 1
        for i, item in enumerate(prefix_sum):
            prefix_sum[i] = accumulator + item
            accumulator = prefix_sum[i]
        prefix_sum.sort(reverse=True)

        for i in range(len(nums)):
            if prefix_sum[i] == 0:
                break
            _sum += prefix_sum[i]*nums[i]
        return _sum%(10**9 + 7)