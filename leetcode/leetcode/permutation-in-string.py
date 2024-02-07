class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        '''
        initialize currCount, lookup, l, r, flag
        '''

        currCount = Counter(s2[:len(s1)])
        lookup = Counter(s1)

        l = 0
        r = len(s1)
        flag = False

        for s in currCount:
            if lookup[s] == currCount[s]:
                flag = True
            else:
                flag = False
                break
        if flag:
            return True

        while r < len(s2):
            currCount[s2[r]] += 1
            currCount[s2[l]] -= 1
            for s in currCount:
                if lookup[s] == currCount[s]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                return True
            r += 1
            l += 1
        return False


        