class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        identical = set()
        min_good_integer = float("inf")

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                identical.add(fronts[i])
        
        for i in range(len(fronts)):
            
            if backs[i] not in identical and fronts[i] not in identical:
                min_good_integer =  min(min(backs[i], fronts[i]), min_good_integer)
            elif fronts[i] not in identical:
                min_good_integer = min(fronts[i], min_good_integer)
            elif backs[i] not in identical:
                min_good_integer = min(backs[i], min_good_integer)
            
            

        
        
        return 0 if min_good_integer == float("inf") else min_good_integer
        