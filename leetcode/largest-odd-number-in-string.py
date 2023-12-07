class Solution:
    def largestOddNumber(self, num: str) -> str:

        odd_set = set("13579")

        for i in range(len(num) - 1, -1, -1):
            if num[i] in odd_set:
                return num[:i + 1]
        
        return ""


       