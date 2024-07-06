class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char_count = {}
        t_char_count = {}

        for i in range(len(s)):
            s_char_count[s[i]] = 1 + s_char_count.get(s[i], 0)
            t_char_count[t[i]] = 1 + t_char_count.get(t[i], 0)
        
        return s_char_count == t_char_count
