from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def build_graph(equations, values):
            graph = defaultdict(dict)
            for (dividend, divisor), value in zip(equations, values):
                graph[dividend][divisor] = value
                graph[divisor][dividend] = 1 / value
            return graph

        def bfs(graph, start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            return -1.0

        graph = build_graph(equations, values)
        results = []
        for dividend, divisor in queries:
            results.append(bfs(graph, dividend, divisor))
        return results

# Test the function with the provided test case
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

solution = Solution()
output = solution.calcEquation(equations, values, queries)
print(output)  # Expected: [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]