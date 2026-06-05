from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        dict = {}
        left = 0
        right = 0
        max_length = 0
        while right < len(nums):
            if nums[right] - nums[left] == 1:
                max_length = max(max_length, right - left + 1)
                dict[nums[right]] = dict.get(nums[right], 0) + 1
            elif nums[right] - nums[left] > 1:
                dict[nums[left]] = dict.get(nums[left], 0) - 1
                left += 1
            right += 1

        return max_length

x = Solution()
print(x.findLHS([1,2,2,1])) # 4
    

