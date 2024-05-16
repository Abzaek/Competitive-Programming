class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(count, valid):

            if count[1] > count[0] or count[0] > n:
                return
            if len(valid) == 2*n:
                ans.append(valid.copy())
                return
            
            count[0] += 1
            valid.append('(')
            backtrack(count, valid)
            count[0] -= 1
            count[1] += 1
            valid.pop()
            valid.append(')')
            backtrack(count, valid)
            valid.pop()
            count[1] -= 1

        backtrack([0,0], [])

        return [''.join(ar) for ar in ans]


                    


        