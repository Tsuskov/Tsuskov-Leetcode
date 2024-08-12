from typing import List

from numpy import sort


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sd = {} # sorted dictionary key is the sorted word and value is the list of words that are anagrams of the key
        for word in strs: # for each word in the list of words
            sorted_word = ''.join(sorted(word)) # sort the word
            if sorted_word not in sd: # if the sorted word is not in the dictionary
                sd[sorted_word] = [word] # add the sorted word as a key and the word as a value
            else:
                sd[sorted_word].append(word) # if the sorted word is in the dictionary, append the word to the value
        return list(sd.values()) # return the values of the dictionary as a list
     

x = Solution()
x.groupAnagrams(["eat","tea","tan","ate","nat","bat"])