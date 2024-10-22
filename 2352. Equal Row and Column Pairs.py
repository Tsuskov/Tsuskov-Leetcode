from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        # Create a list of columns
        columns = [[grid[row][col] for row in range(n)] for col in range(n)]
        
        # Compare each row with each column
        for row in grid:
            for col in columns:
             if row == col:
                count += 1
        
        return count