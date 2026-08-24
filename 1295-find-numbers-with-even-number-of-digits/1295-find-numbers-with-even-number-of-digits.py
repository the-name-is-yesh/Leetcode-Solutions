class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            x = len(str(i))
            if x % 2 == 0:
                cnt+=1
        return cnt