class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        even = []
        odd = []
        for i in s:
            if i  not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in freq.values():
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        esum = sum(even)
        osum = 0
         
        for i in odd:
            osum += i-1
        
        if odd:
            return esum + osum + 1
        else:
            return esum

                
        