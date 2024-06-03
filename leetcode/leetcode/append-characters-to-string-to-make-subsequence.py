class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pntr = 0
        N = len(t)

        for i in range(len(s)):
            if pntr == N:
                return 0

            if s[i] == t[pntr]:
                pntr += 1
                
        return N - pntr
        