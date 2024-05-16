class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ind = 0
        for push in pushed:
            stack.append(push)

            while ind < len(popped) and stack and stack[-1] == popped[ind]:
                stack.pop()
                ind += 1
        
        return not stack

        