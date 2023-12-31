

# Leetcode : https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        f_index={}
        result= -1

        for i in range(len(s)):
            if s[i] in f_index:
                result=max(result,i-f_index[s[i]]-1)
            else:
                f_index[s[i]]=i

        return result
