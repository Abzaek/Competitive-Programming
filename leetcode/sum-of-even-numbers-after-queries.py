class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        '''
        the ith index was previously odd and when it is add up with query[i] it becomes even, so we increase the even sum with the new value

        the ith element was even and add up it becomes odd therefore we subtract the element from the even sum

        the ith element was even and when added up it becomes even, so we increas by the difference of the two(the new - the old)

        the ith element was odd and when added it becomes odd, so we do nothing
        '''

        ans = []
        even_sum = sum([i for i in nums if i % 2 == 0])


        for i, j in queries:
            if nums[j] % 2 and i % 2:
                even_sum += nums[j] + i
                nums[j] = nums[j] + i
            elif nums[j] % 2 and i % 2 == 0:
                nums[j] = nums[j] + i
            elif nums[j] % 2 == 0 and i % 2:
                even_sum -= nums[j]
                nums[j] = nums[j] + i
            else:
                even_sum += i
                nums[j] = nums[j] + i
            ans.append(even_sum)

        return ans
