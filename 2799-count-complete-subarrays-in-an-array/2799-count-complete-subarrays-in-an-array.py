class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        diff = len(set(nums))
        left = 0
        freq = {}
        dist = 0
        cnt = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
            if freq[nums[i]] == 1:
                dist+=1
            
            while dist == diff:
                cnt+=len(nums)-i

                freq[nums[left]]-=1
                if freq[nums[left]] == 0:
                    dist -= 1
                left += 1
        return cnt