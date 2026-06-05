class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        pairs = []
        for a, b in zip(s1, s2):
            if a != b:
                pairs.append((a, b))
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
