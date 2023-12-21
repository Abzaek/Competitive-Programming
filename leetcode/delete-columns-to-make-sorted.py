class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        _count = 0

        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    _count += 1
                    break

        return _count

        