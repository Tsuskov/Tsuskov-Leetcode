from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1  # We can delete at most one element
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_len = max(max_len, right - left)

        return max_len