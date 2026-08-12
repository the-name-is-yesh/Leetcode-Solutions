class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid[0])
        n = len(grid)
        res = []
        ans = []
        k = k % (m * n)
        for i in grid:
            for j in i:
                res.append(j)
        res = res[-k:]+res[:-k]

        for i in range(0,m*n,m):
            ans.append(res[i:i+m])

        return ans
