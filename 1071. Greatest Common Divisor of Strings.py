import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # If the concatenation of str1 and str2 is not equal to the concatenation of str2 and str1
            return '' # Return an empty string
        return str1[:math.gcd(len(str1), len(str2))] # Return the substring of str1 from index 0 to the greatest common divisor of the lengths of str1 and str2
    