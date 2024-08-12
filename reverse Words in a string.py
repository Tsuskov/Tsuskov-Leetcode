class Solution:
 def reverseWords(self, s: str) -> str:
                return ' '.join(s.split()[::-1])  # Split the string by space, reverse the list, and join the elements by space


    
x = Solution()
print(x.reverseWords("the sky is blue")) # blue is sky the