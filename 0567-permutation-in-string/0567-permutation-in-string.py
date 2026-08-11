from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        dict1 = Counter(s1)
        freq = {}
        k = len(s1)

        for i in range(len(s2)):
            if s2[i] in freq:
                freq[s2[i]]+=1
            else:
                freq[s2[i]]=1
            
            if i-left+1 > k:
                freq[s2[left]]-=1

                if freq[s2[left]]==0:
                    del freq[s2[left]]
                left+=1
            if freq == dict1:
                return True
        return False