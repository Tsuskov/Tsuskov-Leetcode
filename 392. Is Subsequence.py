class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
     s_pointer, t_pointer = 0, 0
    
     while t_pointer < len(t):
        if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1