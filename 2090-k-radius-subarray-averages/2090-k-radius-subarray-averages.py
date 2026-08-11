class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]*len(nums)
        x = 2*k + 1
        
        if x > len(nums):
            return ans
        
       

        su = sum(nums[:x])
        avg = su // x
        ans[k] = avg

        for i in range(x,len(nums)):
            su += nums[i]
            su -= nums[i-x]

            centre = i-k

            ans[centre] = su // x

        return ans
        