#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:54:58 2021

@author: eeshaahluwalia
"""


import points


#Rectangle

class rectangle(points.shape.shape):
    
    def __init__(self,Width,Height,topLeftPoint,fillColor='Red', strokeColor='Blue', strokeWidth=5):
        self.Width=Width
        self.Height=Height
        self.topLeftPoint=topLeftPoint
        super().__init__(fillColor, strokeColor, strokeWidth)
    def area(self):
        return self.Width*self.Height
    def centroid(self):
        return points.Point(self.topLeftPoint.getX()+self.Width/2,self.topLeftPoint.getY()+self.Height/2)
    def toString(self):
        return "rectangle", self.Width, self.Height, self.topLeftPoint.toString()
    def contains(self,point):
        if point.getX()>self.topLeftPoint.getX() and point.getX()<self.topLeftPoint.getX()+self.Width and point.getY()>self.topLeftPoint.getY() and point.getY()<self.topLeftPoint.getY()+self.Height:
            return True
        else:
            return False
    def perimeter(self):
        return 2*self.Width+2*self.Height
    def gettopLeftPoint(self) -> points.Point:
        return self.topLeftPoint
    def getWidth(self):
        return self.Width
    def getHeight(self):
        return self.Height
    def settopLeftPoint(self, topLeftPoint):
        self.topLeftPoint=topLeftPoint
    def setWidth(self, Width):
        self.Width=Width
    def setHeight(self, Height): 
        self.Height=Height
