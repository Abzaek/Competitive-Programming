class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        1 0 0
        '''
        ones = 0
        total = 0

        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            else:
                total += ones
        return total