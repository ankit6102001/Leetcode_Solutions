

# Leetcode : https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        required_chars = Counter(t)
        left, right = 0, 0
        formed_chars = 0
        window_counts = {}
        ans = float('inf'), 0, 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if window_counts[char] == required_chars[char]:
                formed_chars += 1
            while formed_chars == len(required_chars):
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right + 1)

                char = s[left]
                window_counts[char] -= 1

                if window_counts[char] < required_chars[char]:
                    formed_chars -= 1

                left += 1

            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]
