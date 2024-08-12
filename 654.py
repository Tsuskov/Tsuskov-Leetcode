from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicates = set()
        result = []
        for num in nums:
            if num in duplicates:
                result.append(num)
            duplicates.add(num)
        for i in range(1, len(nums) + 1):
            if i not in duplicates:
                result.append(i)
                break
        return result
        
x = Solution()
print(x.findErrorNums([1,2,2,4])) # [2,3]