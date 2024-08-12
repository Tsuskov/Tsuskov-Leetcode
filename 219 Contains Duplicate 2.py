from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = dict()
        for i in range(len(nums)):
            if nums[i] in D:
                if i - D[nums[i]] <= k:
                    return True
            D[nums[i]] = i
        
        return False
x = Solution()
print (x.containsNearbyDuplicate([2,3,4,2],4))
