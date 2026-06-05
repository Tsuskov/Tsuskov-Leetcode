# Mock implementation of the guess API
def guess(num: int) -> int:
    # This is a placeholder implementation.
    # Replace this with the actual logic or import the function if defined elsewhere.
    target = 6  # Example target number
    if num < target:
        return 1
    elif num > target:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
             return mid
            elif res < 0:
             right = mid - 1
            else:
             left = mid + 1