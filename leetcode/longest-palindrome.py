class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        lookup = Counter(s)
        
        for i in lookup:
            if lookup[i] > 1:
                ans += (lookup[i]//2)*2
        
        if ans < len(s):
            return ans + 1
        
        return ans
                
        