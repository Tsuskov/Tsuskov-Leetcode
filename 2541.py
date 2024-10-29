from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Create a list of tuples where each tuple is (nums2[i], nums1[i])
        pairs = list(zip(nums2, nums1))

        # Sort the pairs based on the first element in descending order
        pairs.sort(reverse=True, key=lambda x: x[0])

        # Use a min-heap to keep track of the k largest elements from nums1
        min_heap = []
        current_sum = 0
        max_score = 0

        for i in range(len(pairs)):
            # Add the current nums1 value to the heap and to the current sum
            heapq.heappush(min_heap, pairs[i][1])
            current_sum += pairs[i][1]

            # If the heap size exceeds k, remove the smallest element from the heap and adjust the current sum
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # If the heap size is exactly k, calculate the score and update the max_score if necessary
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * pairs[i][0])

        return max_score