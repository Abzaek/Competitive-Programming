'''

'''

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        _maximum = 0
        

        for _index in range(len(grid) - 2):
            for _col in range(len(grid[0]) - 2):
                curr_sum = 0
                curr_sum += grid[_index][_col] + grid[_index][_col + 1] + grid[_index][_col + 2]
                curr_sum += grid[_index + 1][_col + 1]
                curr_sum += grid[_index + 2][_col] + grid[_index + 2][_col + 1] + grid[_index + 2][_col + 2]
                _maximum = max(curr_sum, _maximum)
        return _maximum

                

        