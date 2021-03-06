class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        
        left = 0
        right = len(s) -1
        
        while left <= right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            
            if lower(s[left]) != lower(s[right]):
                return False
        
            left+=1
            right-=1
            
        return True
