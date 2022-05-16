class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        
        if len(s1) > len(s2):
            return False
        
        s1charcount = [0] * 26
        s2charcount = [0] * 26
        
        for idx in range(len(s1)):
            s1charcount[ord(s1[idx]) - ord("a")] += 1
            s2charcount[ord(s2[idx]) - ord("a")] += 1
        
        matchcount = 0
        for idx in range(26):
            if s1charcount[idx] == s2charcount[idx]:
                matchcount += 1
        
        lidx = 0
        for ridx in range(len(s1), len(s2)):
            if matchcount == 26:
                return True
            
            #right side
            currentcharatidx = ord(s2[ridx]) - ord("a")
            
            existingmatch = False
            if s1charcount[currentcharatidx] == s2charcount[currentcharatidx]:
                existingmatch = True
            
            s2charcount[currentcharatidx] += 1
            if s1charcount[currentcharatidx] == s2charcount[currentcharatidx]:
                matchcount += 1
            elif existingmatch:
                matchcount -= 1
            
            #left side
            currentcharatidx = ord(s2[lidx]) - ord("a")
            
            existingmatch = False
            if s1charcount[currentcharatidx] == s2charcount[currentcharatidx]:
                existingmatch = True
            
            s2charcount[currentcharatidx] -= 1
            if s1charcount[currentcharatidx] == s2charcount[currentcharatidx]:
                matchcount += 1
            elif existingmatch:
                matchcount -= 1
            
            lidx +=1
            
            
        return matchcount == 26
