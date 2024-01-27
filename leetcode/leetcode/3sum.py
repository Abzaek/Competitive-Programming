class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            l = i + 1
            r  = len(nums) - 1
            for j in range(i + 1, len(nums)):
                if r <= l:
                    break
                if nums[i] <= 0:
                    if nums[l] + nums[r] >= 0:
                        if nums[i] + (nums[l] + nums[r]) == 0:
                            if [nums[i], nums[l], nums[r]] not in ans:
                                ans.append([nums[i], nums[l], nums[r]])
                            l += 1
                            r -= 1
                        elif abs(nums[i]) < nums[l] + nums[r]:
                            r -= 1
                        else:
                            l += 1
                    else:
                        l += 1
                else:
                    if nums[l] + nums[r] <= 0:
                        if (nums[i] + nums[l] + nums[r]) == 0:
                            if [nums[i], nums[l], nums[r]] not in ans:
                                ans.append([nums[i], nums[l], nums[r]])
                            l += 1
                            r -= 1
                        elif nums[i] + (nums[l] + nums[r]) > 0:
                            r -= 1
                        else:
                            l += 1
                    else:
                        r -= 1
                
        return ans



                            
