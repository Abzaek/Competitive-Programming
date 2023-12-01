class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabate = list(string.ascii_lowercase)
        hshtbl = {}
        ans = ""

        for i in range(26):
            if i < 9:
                hshtbl[i + 1] = alphabate[i]
            else:
                hshtbl[f'{i + 1}#'] = alphabate[i]
        i = 0
        while i < len(s):
            if i + 2 < len(s):
                if s[i + 2] == "#":
                    ans += hshtbl[s[i:i + 3]]
                    i += 3
                else:
                    ans += hshtbl[int(s[i])]
                    i += 1
            else:
                    ans += hshtbl[int(s[i])]
                    i += 1
        return ans

