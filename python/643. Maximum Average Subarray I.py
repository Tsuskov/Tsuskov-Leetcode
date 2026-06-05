from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0 # sum
        for i in range(k): # loop through the first k elements
            sum += nums[i] # add the element to sum
        max_sum = sum # max sum
        for i in range(k, len(nums)): # loop through the rest of the elements
            sum += nums[i] - nums[i - k] # add the element to sum and subtract the element k elements ago
            max_sum = max(max_sum, sum) # set max_sum to the maximum of max_sum and sum
        return max_sum / k # return max_sum divided by k
    
x = Solution()
print(x.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75
