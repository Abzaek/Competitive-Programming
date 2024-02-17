class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lookup = {'five': 0, 'ten': 0}
        
        for bill in bills:
            if bill == 5:
                lookup['five'] += 1
            elif bill == 10:
                if lookup['five'] == 0:
                    return False
                
                lookup['five'] -= 1
                lookup['ten'] += 1
            else:
                if (not lookup['five'] >= 1) or (lookup['five'] < 3 and lookup['ten'] == 0):
                    return False
                
                if lookup['ten']:
                    lookup['ten'] -= 1
                    lookup['five'] -= 1
                else:
                    lookup['five'] -= 3
        return True
                    