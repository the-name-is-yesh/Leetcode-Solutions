class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        zero = 0
        one = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                zero += 1
            else:
                one+=1

            while zero > k and one > k:
                if s[left] == '0':
                    zero -= 1
                else:
                    one -= 1

                left += 1
            ans += i-left+1
        return ans
            
