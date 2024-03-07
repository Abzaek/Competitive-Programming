class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = defaultdict(int)

        l = 0
        r = 0
        ans = 0
        while r < len(s):
            lookup[s[r]] += 1

            while r - l + 1 - max(lookup.values()) > k:
                lookup[s[l]] -= 1
                if not lookup[s[l]]:
                    del lookup[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans

        
            

        