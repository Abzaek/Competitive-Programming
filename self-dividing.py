class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            sI = str(i)

            for j in range(len(sI)):
                if sI[j] == '0':
                    break
                if i % int(sI[j]) != 0:
                    break
                if j == len(sI) - 1:
                    ans.append(i)
        return ans
