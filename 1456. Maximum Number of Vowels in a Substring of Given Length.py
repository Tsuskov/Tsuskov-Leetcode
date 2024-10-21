class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        vowels_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowels_count += 1
        max_vowels = vowels_count
        for i in range(k, len(s)):
            if s[i] in vowels:
                vowels_count += 1
            if s[i - k] in vowels:
                vowels_count -= 1
            max_vowels = max(max_vowels, vowels_count)
        return max_vowels
    