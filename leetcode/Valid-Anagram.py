class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count_s = {}
        char_count_t = {}
        
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        return sorted(char_count_s.items()) == sorted(char_count_t.items())
