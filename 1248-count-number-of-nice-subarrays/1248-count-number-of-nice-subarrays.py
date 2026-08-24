class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        left = 0
        ans = 0
        even = 0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                cnt+=1
                even  = 0
            while cnt > k:
                if nums[left]%2!=0:
                    cnt-=1
                left+=1
            if cnt == k:
                while nums[left]%2==0:
                    even+=1
                    left+=1
                ans += even+1
        return ans