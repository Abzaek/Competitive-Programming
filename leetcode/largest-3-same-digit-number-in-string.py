class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = 0
        maxgood = 0

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good = num[i: i + 3]
                if type(good) != type(maxgood):
                    maxgood = good
                    continue
                maxgood = str(max(good, maxgood))

        return maxgood if maxgood != 0 else ""

        