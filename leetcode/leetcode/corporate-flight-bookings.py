class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
      ans = [0]*n
      accumulator = 0

      for booking in bookings:
        if booking[1] == n:
          ans[booking[0] - 1] += booking[-1]
          continue
        ans[booking[0] - 1] += booking[-1]
        ans[booking[1]] -= booking[-1]
      for i in range(n):
        ans[i] += accumulator
        accumulator = ans[i]
      return ans



        