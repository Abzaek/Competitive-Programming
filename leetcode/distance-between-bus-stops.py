class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
       psumm  = []
       count = 0
       for i in distance:
           if len(psumm) == 0:
               psumm.append(i)
               count += 1
               continue
            
           psumm.append(psumm[count - 1] + i)
           count += 1
       destination, start  = max(start, destination), min(start, destination)
       if start == 0:
            return min(abs(psumm[destination - 1]), abs(psumm[-1] - psumm[destination - 1]))
       else:
            return min(abs(psumm[destination - 1] - psumm[start - 1]), abs(psumm[-1] - psumm[destination - 1] + psumm[start - 1]))


        