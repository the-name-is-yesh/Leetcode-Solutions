class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        required = len(need)

        min_len = float('inf')
        min_left = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                # Current window is valid
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                # Remove s[left]
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[min_left:min_left + min_len]