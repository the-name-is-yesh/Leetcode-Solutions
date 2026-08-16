class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums.sort()

        longest = 0
        current = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue              # Skip duplicates

            elif nums[i] == nums[i - 1] + 1:
                current += 1

            else:
                longest = max(longest, current)
                current = 0

        longest = max(longest, current)

        return longest+1