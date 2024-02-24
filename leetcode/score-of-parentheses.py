class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append('(')
                continue

            if type(stack[-1]) == int:
                x = stack.pop()
                stack.pop()
                stack.append(2*x)
            else:

                stack.pop()
                stack.append(1)
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.append(sum(temp))
        return stack[-1]