class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        initialize T_max, F_max, l, r, _count
        '''

        T_max = 0
        F_max = 0
        l = 0
        r = 0
        _count = 0

        while r < len(answerKey):
            if answerKey[r] == 'T':
                if _count < k:
                    _count += 1
                else:
                    while _count >= k:
                        if answerKey[l] == 'T':
                            _count -= 1
                        l += 1
                    _count = k
            F_max = max(F_max, r - l + 1)
            r += 1
        r = 0
        l = 0
        _count = 0

        while r < len(answerKey):
            if answerKey[r] == 'F':
                if _count < k:
                    _count += 1
                else:
                    while _count >= k:
                        if answerKey[l] == 'F':
                            _count -= 1
                        l += 1
                    _count = k
            T_max = max(T_max, r - l + 1)
            r += 1
        print(F_max, T_max)
        return max(T_max, F_max)

