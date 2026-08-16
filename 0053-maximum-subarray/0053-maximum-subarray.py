class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            a = max(nums[i],a+nums[i])
            res = max(a,res)
        return res