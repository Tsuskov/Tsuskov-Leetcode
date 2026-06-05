from typing import Mapping

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = dict()
        mt = dict()
        for n, cs in enumerate(s):
            ct = t[n]
            if cs not in ms:
                if ct in mt and mt[ct] != cs:
                    return False
                ms[cs] = ct
                mt[ct] = cs
            elif ms[cs] != ct:
                return False 
        return True  
                
x = Solution()
print(x.isIsomorphic("badc","baba"))
