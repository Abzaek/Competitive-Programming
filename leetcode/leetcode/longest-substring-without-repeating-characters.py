class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        max_length = 0
        lookup = defaultdict(int)

        l = 0 
        r = 0

        while r < len(s):
            if s[r] in lookup:
                while True:
                    del lookup[s[l]]
                    if s[l] == s[r]:
                        l += 1
                        length = r - l
                        break
                    l += 1
                continue

            lookup[s[r]] = 0 
            r += 1
            length += 1
            max_length = max(length, max_length)

        return max_length