class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        prev_len = len(nums1)
        temp_num = [nums1[i] for i in range(m)]
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if not nums2:
                break
            
            if nums2[p2] < temp_num[p1]:
                nums1[p1 + p2] = nums2[p2]
                p2 += 1
            elif nums2[p2] > temp_num[p1]:
                 nums1[p1 + p2] = temp_num[p1]
                 p1 += 1
            else:
                nums1[p1 + p2], nums1[p1 + p2 + 1] = nums2[p2], nums2[p2]
                p1 += 1
                p2 += 1
        if p1 <= m - 1:
            nums1[p1 + p2:] = temp_num[p1:] 
        elif p2 <= n - 1:
            nums1[p1 + p2:] = nums2[p2:] 


