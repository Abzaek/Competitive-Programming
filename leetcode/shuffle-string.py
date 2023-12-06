class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hshmap = {}
        ans = ""

        for i in range(len(indices)):
            hshmap[indices[i]] = s[i]
        
        for i in range(len(indices)):
            ans += hshmap[i]
        
        return ans
