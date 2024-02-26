class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        _sum = 0
        costs.sort(key= lambda x: x[0] - x[1])
        
        for i in range(len(costs)):
            
            if i < len(costs)//2:
                _sum += costs[i][0]
            else:
                _sum += costs[i][1]
        return _sum
            
        