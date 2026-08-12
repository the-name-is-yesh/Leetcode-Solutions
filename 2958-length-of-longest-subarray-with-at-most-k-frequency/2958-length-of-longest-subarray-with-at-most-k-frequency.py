class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = 0
        freq = {}
        for i in range(0,len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            
            while freq[nums[i]] > k:
                freq[nums[left]] -= 1
                left+=1

            cnt  = max(cnt,i-left+1)
        return cnt