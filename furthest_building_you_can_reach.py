# -*- coding: utf-8 -*-
"""Furthest Building You Can Reach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JhVeoGM25AbjjauGKpXEmOw6RZwZ-MxG
"""

# Leetcode :https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for i, (a, b) in enumerate(itertools.pairwise(heights)):
          diff = b - a
          if diff <= 0:
            continue
          heapq.heappush(minHeap, diff)
          if len(minHeap) > ladders:
            bricks -= heapq.heappop(minHeap)
          if bricks < 0:
            return i

        return len(heights) - 1