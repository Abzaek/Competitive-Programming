class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num_of_moves = 0
        
        while target != 1:
            if maxDoubles:
                if target % 2:
                    target -= 1
                    num_of_moves += 2
                    target = target // 2
                else:
                    num_of_moves += 1
                    target = target // 2
                maxDoubles -= 1
            else:
                num_of_moves += target - 1
                return num_of_moves
        
        return num_of_moves
                    
            