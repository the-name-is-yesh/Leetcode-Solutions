class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)
        return ans