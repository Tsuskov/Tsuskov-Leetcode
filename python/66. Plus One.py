from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(result)]

x = Solution()
print(x.plusOne([9,9,9]))