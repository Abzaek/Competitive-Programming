class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        total_sum = 0
        remainders = [0] * k
        remainders[0] = 1

        for num in nums:
            total_sum = (total_sum + num) % k
            if total_sum < 0:
                total_sum += k 
            count += remainders[total_sum]
            remainders[total_sum] += 1

        return count