class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        shash = {}
        thash = {}
        
        for val in s:
            shash[val] = 1 + shash.get(val, 0)
            
        for val in t:
            thash[val] = 1+ thash.get(val, 0)
        
        for val in shash:
            if shash[val] != thash.get(val, 0):
                return False
        return True
