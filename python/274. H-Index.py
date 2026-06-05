from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() # Sort the citations
        n = len(citations) # Get the length of the citations
        left, right = 0, n - 1 # Initialize the left and right pointers
        while left <= right: # While left is less than or equal to right
            mid = (left + right) // 2 # Get the mid index
            if citations[mid] == n - mid: # If citations[mid] is equal to n - mid
                return n - mid # Return n - mid
            elif citations[mid] < n - mid: # If citations[mid] is less than n - mid
                left = mid + 1 # Update the left pointer
            else: # If citations[mid] is greater than n - mid
                right = mid - 1 # Update the right pointer
        return n - left # Return n - left

x = Solution()
print(x.hIndex([3,0,6,1,5])) # 3