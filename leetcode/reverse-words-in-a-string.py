class Solution:
    def reverseWords(self, s: str) -> str:
        lst = [word for word in s.split(" ")]
        ans = ""

        ans = " ".join([word.strip() for word in lst[::-1] if word.strip() != ""])

        return ans
        