class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        if target in ghosts:
            return False


        for i in ghosts:
            if self.distance(i, target) <= self.distance([0, 0], target):
                return False
        return True
        

    def distance(self, l, t):
        x1, y1 = l
        x2, y2 = t

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        return dx + dy
        