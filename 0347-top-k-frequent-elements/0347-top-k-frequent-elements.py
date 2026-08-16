class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        dic = sorted(freq.items(),key=lambda x:x[1],reverse = True)
        arr = []
        for i in range(k):
            arr.append(dic[i][0])
        return arr