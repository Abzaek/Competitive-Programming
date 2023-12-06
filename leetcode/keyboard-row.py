class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_one = set("qwertyuiop")
        row_two = set("asdfghjkl")
        row_three = set("zxcvbnm")
        ans = []
        
        for i in words:
            if set(i.lower()).issubset(row_one) or set(i.lower()).issubset(row_two) or set(i.lower()).issubset(row_three):
                ans.append(i) 
            else: 
                pass
        
        return ans


        