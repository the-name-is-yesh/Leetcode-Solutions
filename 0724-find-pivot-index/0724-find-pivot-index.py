class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lefs = 0
        rigs = 0
        for i in range(len(nums)):
            rigs = total-lefs-nums[i]
            if rigs == lefs:
                return i
            lefs += nums[i]
        return -1