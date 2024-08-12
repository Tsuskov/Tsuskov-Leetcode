from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 # Initialize the i pointer
        for num in nums: # Loop through the list
            if i < 2 or num != nums[i - 2]: # If i is less than 2 or num is not equal to nums[i - 2]
                nums[i] = num # Update the nums[i] to num
                i += 1 # Increment i
        return i # Return i
    
x = Solution()
print(x.removeDuplicates([1,1,1,2,2,3])) # 5