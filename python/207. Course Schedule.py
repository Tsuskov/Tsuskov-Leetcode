from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjazenzliste aufbauen
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        # 0 = unbesucht, 1 = in aktuellem Pfad, 2 = fertig
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:  # Zyklus gefunden!
                return False
            if state[course] == 2:  # bereits geprüft, kein Zyklus
                return True

            state[course] = 1  # aktuellen Pfad markieren
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            state[course] = 2  # fertig
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
