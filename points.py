#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:31:42 2021

@author: eeshaahluwalia
"""
import math
import shape

#Point

class Point(shape.shape):
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
    
