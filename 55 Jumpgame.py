from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) # Get the length of the list
        max_reachable = 0 # Initialize the max_reachable to 0
        for i in range(n): # Loop through the list
            if i > max_reachable: # If i is greater than max_reachable
                return False # Return False
            max_reachable = max(max_reachable, i + nums[i]) # Update the max_reachable to the maximum of max_reachable and i + nums[i]
            if max_reachable >= n - 1: # If the max_reachable is greater than or equal to n - 1
                return True # If the max_reachable is greater than or equal to n - 1, return True