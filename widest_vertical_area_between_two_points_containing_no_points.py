# -*- coding: utf-8 -*-
"""Widest_Vertical_Area_Between_Two_Points_Containing_No_Points.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/177oyfC4WICmfNtaNhhY7z73ohO1FcbEV
"""

#leetcode : https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res=0

        for i in range(len(points)-1):
            res=max(res,points[i+1][0]-points[i][0])

        return res