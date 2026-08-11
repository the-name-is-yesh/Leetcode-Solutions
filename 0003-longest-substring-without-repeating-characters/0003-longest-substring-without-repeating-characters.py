class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        ans = 0

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            
            while freq[s[i]] > 1:
                freq[s[left]] -= 1

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            ans = max(ans,i-left+1)
        return ans
