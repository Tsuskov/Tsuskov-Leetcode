from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reachable = 0 # Initialize the max_reachable to 0
        jumps = 0 # Initialize the jumps to 0
        end = 0 # Initialize the end to 0
        for i in range(n - 1): # Loop through the list
            max_reachable = max(max_reachable, i + nums[i]) # Update the max_reachable to the maximum of max_reachable and i + nums[i]
            if i == end: # If i is equal to end
                jumps += 1 # Increment jumps
                end = max_reachable # Update the end to max_reachable
        return jumps # Return jumps
x = Solution()
print(x.jump([2,3,1,1,4])) # 2