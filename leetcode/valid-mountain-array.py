class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        count = 0
        if len(arr) < 3:
            return False

        for i in range(1, len(arr) - 1):
            if count == 1 and arr[i] < arr[i + 1]:
                return False
            elif arr[i - 1] == arr[i] or arr[i] == arr[i + 1]:
                return False

            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                count += 1
            elif count == 0 and arr[i - 1] > arr[i]:
                return False

        return True if count == 1 else False 