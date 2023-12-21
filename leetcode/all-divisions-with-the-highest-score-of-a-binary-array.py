class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        '''
        [0, 0, 1, 0]
        '''
        hshmp = defaultdict(int)
        hshmp2 = defaultdict(int)
        ans = [0]

        for i in range(1, len(nums) + 1):
            if i == 1 and nums[0] != 0:
                hshmp[i] += hshmp[i - 1] 
            elif nums[i - 1] == 0:
                hshmp[i] += hshmp[i - 1] + 1
            else:
                hshmp[i] += hshmp[i - 1]

        hshmp2[len(nums)] = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                hshmp2[i] += hshmp2[i + 1] + 1
            else:
                hshmp2[i] += hshmp2[i + 1]          


        for i in range(1, len(nums) + 1):
            if hshmp[i] + hshmp2[i] > hshmp[ans[-1]] + hshmp2[ans[-1]]:
                ans.clear()
                ans.append(i)
            elif hshmp[i] + hshmp2[i] == hshmp[ans[-1]] + hshmp2[ans[-1]]:
                ans.append(i)
        return ans
                

