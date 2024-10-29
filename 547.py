from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor, connected in enumerate(isConnected[city]):
                if connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()
        provinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces
