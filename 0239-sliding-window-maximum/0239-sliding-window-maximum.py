class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # ans = []
        # for i in range(0,len(nums)-k+1):
        #     arr = nums[i:i+k]
        #     ans.append(max(arr))
        # return ans

        q = deque()
        ans = []

        for i in range(len(nums)):
            while q and q[0] <= i-k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans

        
            