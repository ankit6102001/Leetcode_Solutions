# Leetcode : https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        s_count = {}
        t_count = {}

        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        steps = 0
        for char, count in s_count.items():
            if char not in t_count or t_count[char] < count:
                steps += count - t_count.get(char, 0)

        return steps
