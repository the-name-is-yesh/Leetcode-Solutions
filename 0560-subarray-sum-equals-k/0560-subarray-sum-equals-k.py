class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        freq = {0:1}
        cnt = 0
        for i in nums:
            pre += i
            if pre - k in freq:
                cnt += freq[pre-k]
            if pre in freq:
                freq[pre] += 1
            else:
                freq[pre] = 1
        return cnt

            
            