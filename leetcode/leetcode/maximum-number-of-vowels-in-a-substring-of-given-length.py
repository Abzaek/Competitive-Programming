class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        initiate max_count, _count, l, r
        '''
        sSet = set()

        for i in ['a', 'e', 'i', 'o', 'u']:
            sSet.add(i)

        _count = 0
        l = 0
        r = 0

        while r < k:
            if s[r] in sSet:
                _count += 1
            r += 1
        max_count = _count
        while r < len(s):
            if s[r] in sSet:
                _count += 1
            if s[l] in sSet:
                _count -= 1
            r += 1
            l += 1
            max_count = max(_count, max_count)

        return max_count
        

        