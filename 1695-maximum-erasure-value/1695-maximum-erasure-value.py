class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        score = 0
        freq = {}
        su = 0
        for i in range(len(nums)):
            su += nums[i]
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            
            while freq[nums[i]] > 1:
                freq[nums[left]]-=1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                su -= nums[left]
                left += 1
            score = max(score,su)
        return score