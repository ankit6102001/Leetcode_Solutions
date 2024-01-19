# -*- coding: utf-8 -*-
"""Minimum Falling Path Sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JhVeoGM25AbjjauGKpXEmOw6RZwZ-MxG
"""

# Leetcode : https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
          for j in range(n):
            mini = math.inf
            for k in range(max(0, j - 1), min(n, j + 2)):
              mini = min(mini, matrix[i - 1][k])
            matrix[i][j] += mini

        return min(matrix[-1])