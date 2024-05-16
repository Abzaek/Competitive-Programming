class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        return self.merge(self.sortArray(nums[:len(nums)//2]), self.sortArray(nums[len(nums)//2:]))
        
    def merge(self, nums1, nums2):
        temp = []
        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                temp.append(nums1[l])
                l += 1
            elif nums2[r] < nums1[l]:
                temp.append(nums2[r])
                r += 1
            else:
                temp.append(nums1[l])
                temp.append(nums1[l])
                l += 1
                r += 1
        while l < len(nums1):
            temp.append(nums1[l])
            l += 1
        while r < len(nums2):
            temp.append(nums2[r])
            r += 1
        return temp
                
                       
                       
            
    
        