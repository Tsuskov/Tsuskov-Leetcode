class Solution:
    def calculate(self, s: str) -> int:
        number = 0 # number
        sign_value = 1 # sign value
        result = 0 # result
        operations_stack = [] # operations stack

        for c in s: # loop through all characters in s
            if c.isdigit(): # if c is a digit
                number = number * 10 + int(c) 
                print(number)
            elif c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
                print(result)
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
                print(operations_stack)
            elif c == ')':
                result += sign_value * number
                result *= operations_stack.pop()
                result += operations_stack.pop()
                number = 0
                print(result)

        return result + number * sign_value
    
x = Solution()
print(x.calculate("1 + 1")) # 2
print(x.calculate(" 2-1 + 2 ")) # 3