class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      
      if len(p) > len(s): return []

      sCount, pCount = {}, {}

      for i in range(len(p)):
          sCount[s[i]] = 1 + sCount.get(s[i], 0)
          pCount[p[i]] = 1 + pCount.get(p[i], 0)

      ans = [0] if sCount == pCount else [] 

      l = 0
      
      for r in range(len(p), len(s)):
          sCount[s[r]] = 1 + sCount.get(s[r], 0)
          sCount[s[l]] = sCount.get(s[l], 0) - 1

          if sCount[s[l]] == 0:
              sCount.pop(s[l])
          l += 1

          if sCount == pCount:
              ans.append(l)
          
          r += 1
      return ans