class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        for i in ghosts:
            if self.distance(i, target) <= self.distance([0, 0], target):
                return False
        return True


    def distance(self, l, t):
      
        return abs(l[0] - t[0]) + abs(l[1] - t[1])
        