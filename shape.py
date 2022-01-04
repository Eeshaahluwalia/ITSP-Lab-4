#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:12:20 2021

@author: eeshaahluwalia
"""

#Shape
class shape():
    def __init__(self,fillColor,strokeColor,strokeWidth):
        self.strokeWidth=strokeWidth
        self.strokeColor=strokeColor
        self.fillColor=fillColor
    def getstrokeWidth(self):
        return self.strokeWidth
    def getstrokeColor(self):
        return self.strokeColor
    def getfillColor(self):
        return self.fillColor
    def setstrokeWidth(self, strokeWidth): 
        self.strokeWidth=strokeWidth
    def setstrokeColor(self, strokeColor): 
        self.strokeColor=strokeColor
    def setfillColor(self, setfillColor): 
        self.fillColor=setfillColor