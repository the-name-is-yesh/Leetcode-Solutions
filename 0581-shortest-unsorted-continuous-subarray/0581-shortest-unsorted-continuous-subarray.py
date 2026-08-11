class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        if nums == sorted(nums):
            return 0
        
        while left < right and nums[left] <= nums[left+1]:
            left+=1

        while right > 0 and nums[right] >= nums[right-1]:
            right-=1
        
        mini = min(nums[left:right+1])
        maxi = max(nums[left:right+1])

        while left > 0 and nums[left-1] > mini:
            left-=1
        while right < n-1 and nums[right+1] < maxi:
            right+=1
        return right-left+1  