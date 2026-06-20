class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zc = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zc +=1
            while zc >1:
                if nums[l] == 0:
                    zc-=1
                l +=1
            res = max(res,r-l)
        return res
        
