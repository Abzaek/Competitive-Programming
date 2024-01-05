class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hshmp1 = {}
        hshmp2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hshmp1:
                if t[i] in hshmp2:
                    return False
                else:
                    hshmp2[t[i]] = s[i]
                hshmp1[s[i]] = t[i]

            else:
                if hshmp1[s[i]] != t[i]:
                    return False
        
        return True
        