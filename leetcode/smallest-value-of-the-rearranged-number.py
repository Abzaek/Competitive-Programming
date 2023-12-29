class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            numArr = [i for i in str(num)[1:]]
        else:
             numArr = [i for i in str(num)]

        if num < 0:
            return -1 * int("".join(sorted(numArr, reverse=True)))
        else:
            numArr.sort()

            for i in range(len(numArr)):
                if numArr[i] != "0":
                    pntr = i
                    numArr[pntr], numArr[0] = numArr[0], numArr[pntr]
                    
                    break
            return int("".join(numArr))


        