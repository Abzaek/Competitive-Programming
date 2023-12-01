class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = num // 3
        if num % 3 == 0:
            return [n - 1, n, n + 1]
        
        return []
        