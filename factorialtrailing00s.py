import string


class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        num = 0
        for i in range(1, n+1):
         fact = fact * i
         print(fact)
        fact_str = str(fact)
        num = len(fact_str) - len(fact_str.rstrip('0'))
        return num

        

x = Solution()
print(x.trailingZeroes(899))