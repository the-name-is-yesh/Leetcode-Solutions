class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in nums:
            if i == 1:
                cnt+=1
                maxi = max(maxi,cnt)
            else:
                cnt = 0
        return maxi