# -*- coding: utf-8 -*-
"""Convert an Array Into a 2D Array With Conditions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgIEQOLSOkaXydrxjlvZcDgT-VplH8Zk
"""

# Leetcode : https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count= defaultdict(int)
        res=[]

        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            count[n]+=1

        return res