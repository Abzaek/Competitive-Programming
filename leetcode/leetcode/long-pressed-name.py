class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l1 = 0 
        l2 = 0
        r1 = 0
        r2 = 0

        while r1 < len(name) and r2 < len(typed):
            if typed[r2] != name[r1]:
                return False
            
            while r1 < len(name) - 1 and name[r1] == name[r1 + 1]:
                r1 += 1
               
            while r2 < len(typed) - 1 and typed[r2] == typed[r2 + 1]:
                r2 += 1
            
            if r2 - l2 < r1 - l1:
                return False
            
            r2 += 1
            r1 += 1
            l1 = r1
            l2 = r2

        print(r1, r2)
        if r2 < len(typed) or r1 < len(name):
            return False
        return True


        