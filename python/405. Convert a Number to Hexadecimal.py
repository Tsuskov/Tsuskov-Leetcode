class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        
        if num < 0:
            num += 2**32
        
        hex_map = '0123456789abcdef'
        res = ''
        
        while num > 0:
            res = hex_map[num % 16] + res
            num //= 16
        
        return res

# Example usage
x = Solution()
print(x.toHex(26))  # Output: "1a"
print(x.toHex(-1))  # Output: "ffffffff"