class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == 'D':
                x = stack[-1]
                stack.append(2*x)
            elif op == 'C':
                stack.pop()
            elif op == '+':
                x = stack[-1]
                y = stack[-2]
                stack.append(x + y)
            else:
                stack.append(int(op))
        return sum(stack)
        