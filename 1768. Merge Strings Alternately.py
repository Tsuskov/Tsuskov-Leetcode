class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = '' # Initialize an empty string
        for i in range(min(len(word1), len(word2))): # Iterate through the length of the shorter word
            res += word1[i] + word2[i] # Concatenate the ith character of word1 and word2
        return res + word1[i + 1:] + word2[i + 1:] # Concatenate the remaining characters of the longer word
    