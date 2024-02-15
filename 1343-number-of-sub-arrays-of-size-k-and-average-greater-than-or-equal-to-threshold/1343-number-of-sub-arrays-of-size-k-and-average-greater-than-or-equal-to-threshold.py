class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        _sum = 0
        ans = 0
        while right < k:
            _sum += arr[right]
            right += 1
        

        while right < len(arr) + 1:
            if _sum >= threshold*k:
                ans += 1
                
            if right < len(arr):
                _sum -= arr[left]
                _sum += arr[right]

            left += 1
            right += 1
        
        return ans
        
        