class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
    
x = Solution()
print(x.addDigits(38)) # 2