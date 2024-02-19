class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        flag = True
        for ast in asteroids:
            
            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    flag = False
                    break
                elif stack[-1] > abs(ast):
                    flag = False
                    break
                else:
                    stack.pop()
                    flag = True
            else:
                flag = True
            if flag:
                stack.append(ast) 
        return stack

        