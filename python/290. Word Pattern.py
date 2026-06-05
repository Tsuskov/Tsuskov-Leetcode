from typing import Mapping

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        ptw = dict()
        wtp = dict() 

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p not in ptw:
                if w in wtp:
                    return False
                ptw[p] = w
                wtp[w] = p
            else:
                if ptw[p] != w:
                    return False
        return True
            
x = Solution()

assert x.wordPattern("a","dog dog dog dog dog") is True
assert x.wordPattern("a", "dog dog dog cat") is True
assert x.wordPattern("abba","dog cat cat dog")  is True
assert x.wordPattern("abba","dog cat cat fish")  is False
assert x.wordPattern("aaaa","dog cat cat dog")  is False

