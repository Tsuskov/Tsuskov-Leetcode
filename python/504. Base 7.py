class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        base7 = ""
        while num > 0:
            base7 = str(num % 7) + base7
            num //= 7
        return "-" + base7 if negative else base7
