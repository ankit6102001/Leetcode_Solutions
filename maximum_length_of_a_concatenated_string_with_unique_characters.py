# -*- coding: utf-8 -*-
"""Maximum Length of a Concatenated String with Unique Characters.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JhVeoGM25AbjjauGKpXEmOw6RZwZ-MxG
"""

# Leetcode : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLength = [0]
        self.backTrack(arr, "", 0, maxLength)
        return maxLength[0]

    def backTrack(self, arr, current, start, maxLength):
        if maxLength[0] < len(current):
            maxLength[0] = len(current)

        for i in range(start, len(arr)):
            if not self.isValid(current, arr[i]):
                continue

            self.backTrack(arr, current + arr[i], i + 1, maxLength)

    def isValid(self, currentString, newString):
        charSet = set()

        for ch in newString:
            if ch in charSet:
                return False

            charSet.add(ch)

            if ch in currentString:
                return False

        return True