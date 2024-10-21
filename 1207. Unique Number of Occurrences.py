from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))