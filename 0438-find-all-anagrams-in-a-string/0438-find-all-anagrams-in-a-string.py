from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p_freq = Counter(p)

        if len(p) > len(s):
            return []

        
        freq = {}
        ans = []

        for i in range(n):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        
        if freq == p_freq:
            ans.append(0)

        
        left = 0

        for i in range(n,len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]] = 1
            freq[s[left]] -= 1
            
            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
            if freq == p_freq:
                ans.append(left)
            
        return ans



            

