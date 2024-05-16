class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l = -1
        r = 10**9
        houses.sort()
        heaters.sort()

        def good(val):
            pointer = 0
            for heater in heaters:
                left = heater - val
                right = heater + val

                if pointer < len(houses) and houses[pointer] < left:
                    return False
                else:
                    while pointer < len(houses) and houses[pointer] >= left and houses[pointer] <= right:
                        pointer += 1

            if pointer < len(houses):
                return False
            return True
        
        while l + 1 < r:
            mid = l + (r - l)//2
            
            if good(mid):
                r = mid
            else:
                l = mid

        return r



        