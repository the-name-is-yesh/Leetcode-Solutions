class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        su = 0
        arr = []
        arr.append(0)
        for i in gain:
            su += i
            arr.append(su)
        print(arr)
        return max(arr)