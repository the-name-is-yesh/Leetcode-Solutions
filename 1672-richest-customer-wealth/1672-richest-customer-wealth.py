class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for i in accounts:
            su = 0
            for j in i:
                su+=j
            res.append(su)
        return max(res)