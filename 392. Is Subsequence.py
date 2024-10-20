class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
     s_pointer, t_pointer = 0, 0
    
     while t_pointer < len(t):
        if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    # Nach dem Durchlaufen von t, prüfen ob alle Zeichen von s gefunden wurden
     return s_pointer == len(s)
