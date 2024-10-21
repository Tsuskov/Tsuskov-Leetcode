class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        return set(counter1.keys()) == set(counter2.keys()) and sorted(counter1.values()) == sorted(counter2.values())

# Test case
word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"
solution = Solution()
print(solution.closeStrings(word1, word2))  # Output: False