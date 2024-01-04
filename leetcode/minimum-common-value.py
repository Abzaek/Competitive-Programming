class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        l = 0
        r = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                r += 1
            elif nums2[r] > nums1[l]:
                l += 1
            else:
                return nums1[l]
        return -1
        