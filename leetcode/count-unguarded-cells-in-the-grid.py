class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        result = 0
        grid = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for row, col in guards:
            grid[row][col] = 'G'

        for row, col in walls:
            grid[row][col] = 'W'

        for i in range(m):
            last_cell = 0
            for j in range(n):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                else:
                    left[i][j] = last_cell
            last_cell = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                else:
                    right[i][j] = last_cell

        for j in range(n):
            last_cell = 0
            for i in range(m):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                else:
                    up[i][j] = last_cell
            last_cell = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    last_cell = grid[i][j]
                else:
                    down[i][j] = last_cell

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and left[i][j] != 'G' and right[i][j] != 'G' and \
                   up[i][j] != 'G' and down[i][j] != 'G':
                    result += 1

        return result
