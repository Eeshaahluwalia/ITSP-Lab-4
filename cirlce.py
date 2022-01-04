#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:31:47 2021

@author: eeshaahluwalia
"""
import math
import points


#Circle

class circle(points.shape.shape):
    def __init__(self,radius,centerPoint,fillColor='Red', strokeColor='Blue', strokeWidth=5):
        self.radius=radius
        self.centerPoint=centerPoint
        super().__init__(fillColor, strokeColor, strokeWidth)
    def getcenterPoint(self) -> points.Point:
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
    
    
