class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        equal = []

        for i in nums:
            if i < pivot:
                less_than.append(i)
            elif i > pivot:
                greater_than.append(i)
            else:
                equal.append(i)
        return less_than + equal + greater_than
        