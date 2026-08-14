class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr = set()
        for i  in range(len(nums)):
            x = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[l] + nums[r] + x
                if s == 0:
                    arr.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    r-=1
        return list(arr)
