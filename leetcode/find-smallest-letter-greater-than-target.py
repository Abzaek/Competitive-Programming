class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        r = len(letters)

        while l + 1 < r:
            mid = l + (r - l)//2

            if letters[mid] <= target:
                l = mid
            else:
                r = mid
        return letters[r%len(letters)]