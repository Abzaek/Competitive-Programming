class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = -1
        end = len(matrix)

        while start + 1 < end:
            mid = start + (end - start)//2

            if matrix[mid][0] <= target:
                start = mid
            else:
                end = mid
        if matrix[start][0] > target:
            return False
        arr = matrix[start]
        l = -1
        r = len(arr)

        while l + 1 < r:
            mid = l + (r - l)//2

            if arr[mid] > target:
                r = mid 
            elif arr[mid] < target:
                l = mid
            else:
                return True
        return False
