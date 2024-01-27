class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = []
        
        # for i in range(min(len(firstList), len(secondList))):

        #     if firstList[i][1] < secondList[i][0] or firstList[i][0] > secondList[i][1]:
            
        #         ans.append([])
        #     else:
        #         curr = []

        #         curr.append(max(firstList[i][0], secondList[i][0]))
        #         curr.append(min(firstList[i][1], secondList[i][1]))
        #         ans.append(curr)
        # return ans

        first = 0
        second = 0

        while first < len(firstList) and second < len(secondList):
            if firstList[first][1] < secondList[second][0]:
                first += 1
            elif secondList[second][1] < firstList[first][0]:
                second += 1
            else:
                curr = []

                curr.append(max(firstList[first][0], secondList[second][0]))
                curr.append(min(firstList[first][1], secondList[second][1]))

                ans.append(curr)

                if firstList[first][1] > secondList[second][1]:
                    second += 1
                elif firstList[first][1] < secondList[second][1]:
                    first += 1
                elif firstList[first][1] == secondList[second][1]:
                    first += 1
                    second += 1
        return ans