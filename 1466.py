from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create adjacency list for the graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # 1 means original direction a -> b
            graph[b].append((a, 0))  # 0 means reverse direction b -> a

        # BFS to count the number of reorders needed
        queue = deque([0])
        visited = set([0])
        reorder_count = 0

        while queue:
            current = queue.popleft()
            for neighbor, direction in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    reorder_count += direction
                    queue.append(neighbor)

        return reorder_count

# Example usage:
solution = Solution()
n1 = 6
connections1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(solution.minReorder(n1, connections1))  # Output: 3

n2 = 5
connections2 = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(solution.minReorder(n2, connections2))  # Output: 2

n3 = 3
connections3 = [[1, 0], [2, 0]]
print(solution.minReorder(n3, connections3))  # Output: 0