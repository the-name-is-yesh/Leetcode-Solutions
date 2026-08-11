from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        word_len = len(words[0])
        word_cnt = len(words)
        tot = word_len * word_cnt

        req = Counter(words)

        for k in range(0,len(s)-tot+1):
            seen = {}

            for j in range(k,k+tot,word_len):
                i = s[j:j+word_len]
                if i not in req:
                    break
                if i in seen:
                    seen[i]+=1
                else:
                    seen[i]=1
                
                if seen[i] > req[i]:
                    break

            else:
                if seen == req:
                    ans.append(k)
        return ans
