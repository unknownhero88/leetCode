class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=len(nums)
        for i in range(0,s):
            for j in range(i+1,s):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
