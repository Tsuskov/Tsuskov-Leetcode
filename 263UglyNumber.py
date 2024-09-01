class Solution:
    def isUgly(self, n: int) -> bool:
        return n > 0 and 30**32 % n == 0
    
x = Solution()
print(x.isUgly(6)) # True
print(x.isUgly(8)) # True
print(x.isUgly(14)) # False
print(x.isUgly(1)) # True
print(x.isUgly(0)) # False
