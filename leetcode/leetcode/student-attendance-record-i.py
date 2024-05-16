class Solution:
    def checkRecord(self, s: str) -> bool:
      A = 0
      L = 0

      r = 0

      while r < len(s):
        while r < len(s) and s[r] == 'L':
          L += 1
          r += 1
          if L >= 3:
            return False
        else:
          if r < len(s) and s[r] == 'A':
            A += 1
        L = 0
        r += 1
      if A < 2:
        return True
      return False
        