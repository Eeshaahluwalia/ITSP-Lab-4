#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:31:47 2021

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


#Circle

class circle(shape):
    def __init__(self,radius,centerPoint,fillColor='Red', strokeColor='Blue', strokeWidth=5):
        self.radius=radius
        self.centerPoint=centerPoint
        super().__init__(fillColor, strokeColor, strokeWidth)
    def getcenterPoint(self) -> Point:
        return self.centerPoint
    def getradius(self):
        return self.radius
    def setcenterPoint(self,centerPoint):
        self.centerPoint=centerPoint
    def setradius(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
    def contains(self,point):
        if point.distance(self.centerPoint)<(self.radius):
            return True
        else:
            return False    
    def toString(self):
        return "Circle", self.centerPoint.toString(), self.radius
    
    
