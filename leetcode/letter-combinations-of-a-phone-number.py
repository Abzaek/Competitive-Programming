class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        lookup = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
        def backtrack(pointer, stack):
            if pointer >= len(digits):
                if stack:
                    ans.append(''.join(stack))
                return 

            for i in range(len(lookup[digits[pointer]])):
                stack.append(lookup[digits[pointer]][i])
                backtrack(pointer + 1, stack)
                stack.pop()
        backtrack(0, [])
        return ans
        
        