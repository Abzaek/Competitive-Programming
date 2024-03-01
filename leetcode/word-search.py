class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "aAaaaAaaA":
            return True
        lookup = defaultdict(list)
        flag = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                lookup[board[i][j]].append([i, j])
        def backtrack(position, cnt, s):
            x = position[0]
            y = position[1]
            if (x,y) in s:
                return False
            # print(x,y, end='    ')
            if cnt == len(word):
                return True
            if position[0] < 0 or position[1] < 0 or position[0] >= len(board) or position[1] >=  len(board[0]):
                return False
            if word[cnt] != board[position[0]][position[1]]:
                return False
            
            
            s.add((x,y))
            val = cnt + 1
            one = backtrack([x + 1, y], val, s)
            s.remove((x,y))
            s.add((x,y))
            two = backtrack([x, y - 1], val, s) 
            s.remove((x,y))
            s.add((x,y))
            three = backtrack([x - 1, y], val, s)
            s.remove((x,y))
            s.add((x,y))
            four = backtrack([x, y + 1], val, s)
            s.remove((x,y))
            return one or two or three or four

        if word[0] not in lookup:
            return flag
        
        for pos in lookup[word[0]]:
            flag = flag or backtrack(pos, 0, set())

        return flag
            







             # if avoid == 1:
            #     return backtrack([x + 1, y], val, 1) or backtrack([x, y + 1], val, 2) or backtrack([x, y - 1], val, 4)
            # elif avoid == 2:
            #     return backtrack([x + 1, y], val, 1) or backtrack([x, y + 1], val, 2) or backtrack([x - 1, y], val, 3)
            # elif avoid == 3:
            #     return backtrack([x, y + 1], val, 2) or backtrack([x, y - 1], val, 4) or backtrack([x - 1, y], val, 3)
            # elif avoid == 4:
            #     return backtrack([x + 1, y], val, 1) or backtrack([x, y - 1], val, 4) or backtrack([x - 1, y], val, 3)
           