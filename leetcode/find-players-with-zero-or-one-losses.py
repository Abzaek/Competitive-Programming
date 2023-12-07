class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        num_of_losses = {}
        all_players = set()

        for i in matches:
            num_of_losses[i[1]] = num_of_losses.get(i[1], 0) + 1
            

            all_players.add(i[0])
        for i in num_of_losses:
            if num_of_losses[i] == 1:
                ans[1].append(i)
            
        for i in all_players:
            if i not in num_of_losses:
                ans[0].append(i)

     
            
        ans[0].sort()
        ans[1].sort() 
        return ans

        