from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies) # Find the maximum number of candies
        return [candy + extraCandies >= max_candies for candy in candies] # Return a list of booleans indicating whether each kid can have the greatest number of candies
    