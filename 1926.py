from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set((entrance[0], entrance[1]))
        
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] == '.':
                    if (nx == 0 or nx == rows - 1 or ny == 0 or ny == cols - 1) and [nx, ny] != entrance:
                        return steps + 1
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))
        
        return -1

# Test case
maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
entrance = [0, 1]
solution = Solution()
print(solution.nearestExit(maze, entrance))  # Expected output: 12