
# Leetcode : https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        sorted_string = ''.join([char * count for char, count in sorted_chars])

        return sorted_string
