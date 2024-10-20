class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)): # Iterate through the flowerbed
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0): # If the current plot is empty and the previous and next plots are empty
                flowerbed[i] = 1 # Plant a flower
                count += 1 # Increment the count
        return count >= n # Return whether the count is greater than or equal to n
    