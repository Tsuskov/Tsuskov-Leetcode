class Solution:
    def isHappy(self, n: int) -> bool:
        m = dict()
        while n != 1:
            if n in m:
                return False
            m[n] = 1
            print(m)
            n = sum([int(x) ** 2 for x in str(n)])
        return True
    

x = Solution()
x.isHappy(19)