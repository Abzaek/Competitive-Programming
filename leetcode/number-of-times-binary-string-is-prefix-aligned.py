class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _max = float('-inf')
        num = 0

        for i in range(len(flips)):
            _max = max(flips[i], _max)
            if i + 1 == _max:
                num += 1
        return num
        