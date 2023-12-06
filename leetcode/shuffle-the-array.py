class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:len(nums)// 2]
        nums = nums[len(nums)//2:]
        ans = []

        print(nums1, nums)

        for i in range(len(nums)):
            ans.append(nums1[i])
            ans.append(nums[i])
        
        return ans

            

        