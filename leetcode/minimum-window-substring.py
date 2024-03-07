class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ss = Counter(t)
        lookup1 = Counter(t)
        lookup2 = defaultdict(int)
        n = len(s)
        m = float('inf')
        l = 0
        r = 0
        ans = ''
        while r < n:
            if s[r] in lookup1:
                lookup1[s[r]] -= 1

                if lookup1[s[r]] == 0:
                    del lookup1[s[r]]
            elif s[r] in ss:
                lookup2[s[r]] += 1
            
            while l < n and (s[l] not in ss or s[l] in lookup2):
                if s[l] in lookup2:
                    lookup2[s[l]] -= 1
                    if not lookup2[s[l]]:
                        del lookup2[s[l]]
                        
                l += 1
            slc = s[l:r + 1]
            if not lookup1 and len(slc) < m:
                ans = slc
                m = len(slc)
            r += 1
        return ans

            
            







        