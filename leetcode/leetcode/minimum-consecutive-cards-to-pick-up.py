class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
      ans = float('inf')

      l = 0
      r = 0
      lookup = set()

      while r < len(cards):
        if cards[r] in lookup:
          while cards[l] != cards[r]:
            lookup.remove(cards[l])
            l += 1
          ans = min(r - l + 1, ans)
          lookup.remove(cards[l])
          l += 1

        lookup.add(cards[r])
        r += 1
      return ans if ans != float('inf') else -1

        