class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:

            tempArr = []

            for i in str(num):
                tempArr.append(int(i))

            num = sum(tempArr)
        return num