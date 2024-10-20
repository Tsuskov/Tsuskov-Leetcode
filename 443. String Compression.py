class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        count = 1
        i = 0
        for j in range(1, len(chars)):
            if chars[j] == chars[i]:
                count += 1
            else:
                if count > 1:
                    for digit in str(count):
                        i += 1
                        chars[i] = digit
                i += 1
                chars[i] = chars[j]
                count = 1
        if count > 1:
            for digit in str(count):
                i += 1
                chars[i] = digit
        return i + 1