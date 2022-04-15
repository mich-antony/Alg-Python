# ref: https://afteracademy.com/blog/valid-anagram
# https://www.youtube.com/watch?v=9UtInBqnCgA
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        strhash = {}
        
        for i in range(len(s)):
            strhash[s[i]] = strhash.get(s[i], 0) + 1            
            strhash[t[i]] = strhash.get(t[i], 0) - 1
        
        for val in strhash:
            if strhash[val] != 0:
                return False
        return True
