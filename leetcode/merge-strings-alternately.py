class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = len(word1)
        m = len(word2)
        for i in range(min(len(word1), len(word2))):
            ans += (word1[i] + word2[i])

        k = min(len(word1), len(word2))

        while n > min(len(word1), len(word2)):
            ans += word1[k]
            k += 1
            n -= 1
        
        while m > min(len(word1), len(word2)):
            ans += word2[k]
            k += 1
            m -= 1
        return ans
