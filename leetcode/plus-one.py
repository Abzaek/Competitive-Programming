class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = ''

        for i in digits:
            d += str(i)
        
        d = str(int(d) + 1)
        ans =[]
        for i in d:
            ans.append(int(i))

        return ans
        