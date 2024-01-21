class Solution:
    def reverseWords(self, s: str) -> str:
        spltd = s.split()

        ans = ['']*len(spltd)

        for n, word in enumerate(spltd):
            for i in range(len(word) - 1, -1, -1):
                ans[n] +=  word[i] 
          
        return ' '.join(ans)
