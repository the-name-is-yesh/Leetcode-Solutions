class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr = []
        n  = len(nums)

        # for i in range(0,n):
        #     for j in range(i,n):
        #         x = nums[i:j+1]
        #         if len(x) == k:
        #             arr.append(sum(x)/k)
        # return max(arr)

        # for i in range(n-k+1):
        #     x = nums[i:i+k]
        #     arr.append(sum(x)/k)
        # return max(arr)

        x = sum(nums[:k])
        su = x
        for i in range(k,n):
            x += nums[i] - nums[i-k]
            su = max(su,x)
        return su/k

        # curr = 0
        # su= 0
        # l = 0
        # for i in range(0,n):
        #     curr += nums[i]
        #     if i-l + 1 == k:
        #         su = max(su,curr)
        #         curr -= nums[l]
        #         l+=1
        # return su/k