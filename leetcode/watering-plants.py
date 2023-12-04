class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        summ = 0
        steps = 0

        for i in range(len(plants) - 1):
            summ += plants[i]
            steps += 1

            if summ + plants[i + 1] > capacity:
                summ = 0
                steps += (i + 1)*2
        return steps + 1
        