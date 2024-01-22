class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        elif word[1:] == word[1:].lower():
            return True
        
        return False