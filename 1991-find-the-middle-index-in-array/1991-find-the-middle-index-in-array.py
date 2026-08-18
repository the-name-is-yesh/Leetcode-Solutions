class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lefs = 0
        total = sum(nums)
        rigs = 0
        for i in range(len(nums)):
            rigs = total-lefs-nums[i]
            if rigs == lefs:
                return i
            lefs += nums[i]
        return -1