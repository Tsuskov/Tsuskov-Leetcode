from typing import List
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums) # convert the list to a set
        longest_streak = 0 # initialize the longest streak to 0
        
        for num in nums: # for each number in the list
            if num - 1 not in m: # if the number minus 1 is not in the set
                current_num = num # set the current number to the number
                current_streak = 1 # set the current streak to 1
                
                while current_num + 1 in m: # while the current number plus 1 is in the set 
                    current_num += 1 # increment the current number by 1
                    current_streak += 1 # increment the current streak by 1
                
                longest_streak = max(longest_streak, current_streak) # set the longest streak to the maximum of the longest streak and the current streak
        
        return longest_streak # return the longest streak

x = Solution()
print(x.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(x.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))