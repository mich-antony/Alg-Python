class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        repeatset = set()
        maxlen = 0
        
        l=0
        r=0
        while (r < len(s)):
            if s[r] not in repeatset:
                repeatset.add(s[r])     
                maxlen = max(maxlen, r-l + 1)
                r += 1                
            else:
               repeatset.remove(s[l])
               l += 1                
        return maxlen
