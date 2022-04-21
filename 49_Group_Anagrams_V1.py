class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        
        res = []
        myd = {}
        
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if not s in myd:
                myd[s] = []
            myd[s].append(i)
        # print (myd)
        for idxs in myd.values():
            tres=[]
            for idx in idxs:
                tres.append(strs[idx])
            res.append(tres)
        # print (res)
        return res
