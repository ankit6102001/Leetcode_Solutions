# -*- coding: utf-8 -*-
"""Rearrange Array Elements by Sign.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JhVeoGM25AbjjauGKpXEmOw6RZwZ-MxG
"""

# Leetcode :https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos = []
        neg = []

        for num in nums:
          (pos if num > 0 else neg).append(num)

        for p, n in zip(pos, neg):
          ans += [p, n]

        return ans