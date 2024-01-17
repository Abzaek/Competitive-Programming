class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        temp_num = []

        for i in nums:
            if i != val:
                k += 1
                temp_num.append(i)
        while len(temp_num) < len(nums):
            temp_num.append("_")
        nums[:len(nums)] = temp_num[:len(temp_num)]
        return k

        