from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) # Get the length of the list
        k %= n # Get the resr of k and n
        self.reverse(nums, 0, n - 1) # Reverse the entire list
        self.reverse(nums, 0, k - 1) # Reverse the first k elements
        self.reverse(nums, k, n - 1) # Reverse the remaining elements

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end: # While start is less than end
            nums[start], nums[end] = nums[end], nums[start] # Swap the elements
            start += 1 # Increment start
            end -= 1 # Decrement end

x = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
x.rotate(nums, k)
print(nums) # [5,6,7,1,2,3,4]    
