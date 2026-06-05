from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: # loop through all tokens
            if token not in "+-*/": # if token is not in "+-*/"
                stack.append(int(token)) # append token to stack
            else: # else
                num2 = stack.pop() # pop stack and set it to num2
                num1 = stack.pop() # pop stack and set it to num1
                if token == "+": # if token is "+"
                    stack.append(num1 + num2) # append num1 + num2 to stack
                elif token == "-": # if token is "-"
                    stack.append(num1 - num2) # append num1 - num2 to stack
                elif token == "*": # if token is "*"
                    stack.append(num1 * num2) # append num1 * num2 to stack
                else: # else
                    stack.append(int(num1 / num2)) # append num1 / num2 to stack
        return stack[0] # return stack[0]

x = Solution()
