class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left  = 0
        cursum = 0
        minlen = float('inf')
        for i in range(len(nums)):
            cursum += nums[i]
            while cursum >= target:
                minlen = min(minlen,i-left+1)
                cursum -= nums[left]
                left += 1
    

        if minlen != float('inf'):
            return minlen
        return 0