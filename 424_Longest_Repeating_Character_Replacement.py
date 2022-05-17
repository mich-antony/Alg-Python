class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charcount = {}
        
        maxlen = 0
        maxcharfreq = 0
        
        l = 0
        
        for r in range(len(s)):
            
            charcount[s[r]] = 1 + charcount.get(s[r] , 0)
            maxcharfreq = max(maxcharfreq, charcount[s[r]])
            
            currentwindowsize = r - l + 1            
            if currentwindowsize - maxcharfreq > k:
                charcount[s[l]] -= 1
                l +=1
                currentwindowsize -= 1
            
            maxlen = max(maxlen, currentwindowsize)
        
        return maxlen
