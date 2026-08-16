class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i in range(len(s)):
            last[s[i]] = i
        
        ans = []
        end = 0
        start = 0

        for i in range(len(s)):
            end = max(end,last[s[i]])
            if i == end:
                ans.append(end-start+1)
                start = i+1
        return ans