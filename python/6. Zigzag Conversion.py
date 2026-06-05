class Solution:
    def convert(self, s: str, numRows: int ) -> str:
        if numRows == 1 or numRows >= len(s): # If numRows is 1 or numRows is greater than or equal to the length of s
            return s # Return s
        zigzag = ['' for _ in range(numRows)] # Create a list of empty strings with numRows elements
        row, step = 0, 1 # Initialize the row and step to 0 and 1 respectively
        for char in s: # Loop through the characters in s
            zigzag[row] += char # Add the character to the row
            if row == 0: # If row is 0
                step = 1 # Set the step to 1
            elif row == numRows - 1: # If row is numRows - 1
                step = -1 # Set the step to -1
            row += step # Update the row
        return ''.join(zigzag) # Join the elements in the zigzag list and return it

x = Solution()
print(x.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR