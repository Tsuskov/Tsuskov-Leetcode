class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            n = len(str(num))
            if n < 3:
                return 0
            s = str(num)
            ans = 0
            for i in range(1, n-1):
                if (s[i-1] < s[i] > s[i+1]) or (s[i-1] > s[i] < s[i+1]):
                    ans += 1
            return ans

        return sum(waviness(i) for i in range(num1, num2 + 1))
        