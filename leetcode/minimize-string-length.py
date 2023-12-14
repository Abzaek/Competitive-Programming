class Solution:
    def minimizedStringLength(self, s: str) -> int:
        counter = 0
        sMap = defaultdict(int)

        for i in s:
            sMap[i] += 1
        for i in sMap:
            counter += 1
        return counter
        # counter = 0

        

        # for char in sMap:
        #     if sMap[char] % 2 and sMap[char] >1:
        #         counter += 1
        #     elif sMap[char] % 2 == 0 and sMap[char] > 2:
        #         counter += 2
        #     else:
        #         counter += 1
        # return counter
        
        