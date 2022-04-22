class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        tempprod = 1
        for i in range(len(nums)):
            res[i] = tempprod
            tempprod = tempprod * nums[i]        
        
        tempprod = 1
        for i in range(len(nums)-1, -1,-1):            
            res[i] = res[i] * tempprod
            tempprod = tempprod * nums[i]        
        
        return res
