class Solution:
  def addSpaces(self, s: str, spaces: List[int]) -> str:
      ans = ""

      for i in range(len(spaces)):
          ans += s[len(ans) - i:spaces[i]] + " "
          

          
          if spaces[i] == spaces[-1]:
              ans += s[len(ans) - i - 1:]

      return ans
    