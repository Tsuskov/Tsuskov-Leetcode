class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sd[i] = s[i]
        for i in range(len(s)):
            for key, value in sd.items():
                if t[i] == value:
                    del sd[key]
                    break
        return len(sd) == 0

x = Solution()
print(x.isAnagram("abb", "bba"))