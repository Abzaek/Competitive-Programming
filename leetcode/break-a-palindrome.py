class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''

        '''
        ans = []
        flag = False

        for i, p in enumerate(palindrome):
            if flag:
                ans.append(p)
            else:
                if len(palindrome) % 2 and i == len(palindrome) // 2:
                    ans.append(p)
                    continue
                elif p != 'a':
                    flag = True
                ans.append('a')

        if ''.join(ans) == palindrome:
            if len(ans) > 1:
                ans[-1] = 'b'
            else:
                return ''

        return ''.join(ans)


        