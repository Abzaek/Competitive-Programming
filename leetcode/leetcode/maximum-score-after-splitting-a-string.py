class Solution:
    def maxScore(self, s: str) -> int:
        l_p = [0]*len(s)
        r_p = [0]*len(s)
        acc = 0
        _max = float('-inf')

        for i in range(len(s)):
            if s[i] == '1':
                r_p[i] = 1 
            
            if i == 0:
                continue
            if s[i - 1] == '0':
                l_p[i] = 1
        l_p = list(accumulate(l_p))
        for i in range(len(s) - 1, -1, -1):
            r_p[i] = acc + r_p[i]
            acc = r_p[i]
        
        for i in range(1, len(s)):
            _max = max(l_p[i] + r_p[i], _max)
        return _max


        