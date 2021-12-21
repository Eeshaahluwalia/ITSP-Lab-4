#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:54:58 2021

@author: eeshaahluwalia
"""
import math

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
        self.setfillColor=setfillColor
        
#Point
class Point(shape):
  def __init__(self, x,y,fillColor='Red', strokeColor='Blue', strokeWidth=5):
    self.x = x
    self.y = y
    super().__init__(fillColor, strokeColor, strokeWidth)
  def setPosition(self,x,y):
    self.x = x
    self.y = y
  def toString(self):
    return "Point (",self.x, self.y,")"
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def setX(self,x):
    self.x=x
  def setY(self,y):
    self.y=y
  def distance(self,p1)-> float:
    return round (math.sqrt((self.x- p1.getX())**2 + (self.y-p1.getY())**2),2)

#Rectangle

class rectangle(shape):
    
    def __init__(self,Width,Height,topLeftPoint,fillColor='Red', strokeColor='Blue', strokeWidth=5):
        self.Width=Width
        self.Height=Height
        self.topLeftPoint=topLeftPoint
        super().__init__(fillColor, strokeColor, strokeWidth)
    def area(self):
        return self.Width*self.Height
    def centroid(self):
        return Point(self.topLeftPoint.getX()+self.Width/2,self.topLeftPoint.getY()+self.Height/2)
    def toString(self):
        return "rectangle", self.Width, self.Height, self.topLeftPoint.toString()
    def contains(self,point):
        if point.getX()>self.topLeftPoint.getX() and point.getX()<self.topLeftPoint.getX()+self.Width and point.getY()>self.topLeftPoint.getY() and point.getY()<self.topLeftPoint.getY()+self.Height:
            return True
        else:
            return False
    def perimeter(self):
        return 2*self.Width+2*self.Height
    def gettopLeftPoint(self) -> Point:
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
