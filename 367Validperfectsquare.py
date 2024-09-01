import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num > 0 and math.isqrt(num) ** 2 == num

        return num > 0 and 30**32 % num == 0
x = Solution()
print(x.isPerfectSquare(16)) # True
print(x.isPerfectSquare(5)) # False
