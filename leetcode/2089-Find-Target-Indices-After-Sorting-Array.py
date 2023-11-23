class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        count = [0]* 100

        for num in nums:
            count[num - 1] += 1

        prefixSum = [count[0]]

        if target == 1:
            index = 0
        else:
            index = target - 2

        for c in range(len(count)):
            if c == 0:
                continue
            prefixSum.append(prefixSum[c - 1] + count[c])
        
        
        while count[target - 1] > 0:
            if target == 1:
                ans.append(index)
                count[target - 1] -= 1
                index += 1
                continue
            
            if len(ans) == 0:
                ans.append(prefixSum[index])
            else:
                ans.append(ans[-1] + 1)

            count[target - 1] -= 1
            index += 1

        return ans
