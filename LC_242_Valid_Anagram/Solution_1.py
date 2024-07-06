class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        for c in s:
            char_count[c] = 1 + char_count.get(c, 0)

        for c in t:
            char_count[c] = char_count.get(c, 0) - 1
            if char_count[c] < 0:
                return False 
        
        return True
