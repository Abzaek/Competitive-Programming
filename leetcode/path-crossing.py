class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        x = 0
        y = 0
        s.add(f'{x},{y}')
        for i in path:
            if i == "E":
                x += 1
            elif i == "N":
                y += 1
            elif i == "W":
                x -=  1
            else:
                y -= 1
            if f'{x},{y}' in s:
                return True
            s.add(f'{x},{y}')
        return False


        