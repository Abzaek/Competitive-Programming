class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hshtbl = {}

        for ind, i in enumerate(order):
            hshtbl[i] = ind

        for i in range(len(words) - 1):
            
            for j in range(min(len(words[i]), len(words[i + 1]))):

                if hshtbl[words[i][j]] == hshtbl[words[i + 1][j]]:
                    if j == min(len(words[i]), len(words[i + 1])) - 1 and min(len(words[i]), len(words[i + 1])) == len(words[i + 1]) and len(words[i + 1]) != len(words[i]):
                        return False
                    else:
                        continue
                else:
                    if hshtbl[words[i][j]] > hshtbl[words[i + 1][j]]:
                        return False
                    else:
                        break
        return True
            
            
            

            


        