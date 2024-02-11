class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0]*1001
        accumulator = 0

        for i in range(len(trips)):
          car[trips[i][1]] += trips[i][0]
          car[trips[i][2]] -= trips[i][0]
        
        for i in range(1001):
          car[i] += accumulator
          accumulator = car[i]

          if car[i] > capacity:
            return False
        return True
        