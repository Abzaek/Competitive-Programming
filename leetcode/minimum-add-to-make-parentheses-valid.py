class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        lookup = defaultdict()
        lookup['('] = 0
        ans = 0
        
        for i in s:
            if i == '(':
                lookup['('] += 1
            else:
                if lookup['(']:
                    lookup['('] -= 1
                else:
                    ans += 1
        
        return ans + lookup['(']
                    
        
        
        