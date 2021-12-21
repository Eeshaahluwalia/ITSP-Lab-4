#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:50:24 2021

@author: eeshaahluwalia
"""


import unittest

import points 

import rectangle

import cirlce

import shape

import math

#All imports of cirlce, rectange and points classes have inherited the shape.
#Part 4.a

class TestPoint(unittest.TestCase):

    def test_get_X(self):
        test_point  =  points.Point(20, 45)
        return self.assertEqual(20, test_point.getX())
#Part 4.c
#Point functions

    def test_get_Y(self):
        test_point  =  points.Point(15, 40)
        return self.assertEqual(40, test_point.getY())
       
    def test_set_X(self):
        test_point  =  points.Point(20, 45)
        test_point.setX(25)
        return self.assertEqual(25, test_point.getX())
    
    def test_set_Y(self):
        test_point  =  points.Point(15, 40)
        test_point.setY(20)
        return self.assertEqual(20, test_point.getY()) 
    
    def test_set_Position(self):
        test_point  =  points.Point(15, 40)
        test_point.setPosition(20, 50)
        return (self.assertEqual(20, test_point.getX()) and self.assertEqual(50, test_point.getY()))
    
    
    def test_distance(self):
        test_point  =  points.Point(15, 40)
        test_point2  =  points.Point(35, 20)
        return self.assertEqual(round(((15-35)**2 + (40-20)**2)**0.5, 2), test_point.distance( test_point2))
    
             
#Rectangle function


    def test_get_top_Left_Point(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(15, test_point.gettopLeftPoint().getX())
    
    def test_get_Width(self):
        test_point  =  rectangle.rectangle(20,45, points.Point(15, 40))
        return self.assertEqual(20, test_point.getWidth())   
    
    def test_get_Height(self):
        test_point  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(45, test_point.getHeight())    
    
    def test_set_top_Left_Point(self):
        test_point  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.settopLeftPoint(15)
        return self.assertEqual(15, test_point.gettopLeftPoint())
    
    def test_set_Width(self):
        test_point  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.setWidth(20)
        return self.assertEqual(20, test_point.getWidth())
    
    def test_set_Height(self):
        test_point  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.setHeight(45)
        return self.assertEqual(45, test_point.getHeight())
    
    def test_area_rect(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(900, test_point.area())
        
    def test_centroid(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        point= test_point.centroid()
        return self.assertEqual(test_point.gettopLeftPoint().getX()+ test_point.getWidth()/2,point.getX()) and self.assertEqual(test_point.gettopLeftPoint().getY()+ test_point.getHeight()/2,point.getY())

        
    def test_contains_rect(self):
        test_point = rectangle.rectangle(1, 1, points.Point(15, 40))
        return self.assertEqual(False, test_point.contains(points.Point(-1,-1)))
        
    def test_perimeter_rect(self):
        test_point= rectangle.rectangle(20,45, points.Point(10, 45))
        return self.assertEqual(130, test_point.perimeter())

    
#Circle function 

    def test_get_center_Point(self):
        test_point = cirlce.circle(20, points.Point(10, 45))
        return (self.assertEqual(10, test_point.getcenterPoint().getX()) and self.assertEqual(45, test_point.getcenterPoint().getY()))
    
    def test_get_radius(self):
        test_point = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(20, test_point.getradius())
    
    def test_set_center_Point(self):
        test_point  =  cirlce.circle(20, points.Point(10, 45))
        test_point.setcenterPoint(20)
        return self.assertEqual(20, test_point.getcenterPoint())
    
    def test_set_radius(self):
        test_point  =  cirlce.circle(20, points.Point(10, 45))
        test_point.setradius(20)
        return self.assertEqual(20, test_point.getradius())
    
    def test_area_circle(self):
        test_point = cirlce.circle(20, points.Point(15, 40))
        return self.assertEqual(math.pi*20**2,test_point.area())
        
    def test_perimeter_cirlce(self):
        test_point= cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(20*2*math.pi, test_point.perimeter())
        
    def test_contains_circle(self):
        test_point = cirlce.circle(2, points.Point(15, 40))
        return self.assertEqual(True, test_point.contains(points.Point(16,41)))

          
   #Shapes for the original classes

    def test_getstrokeWidth(self):
        test_point = shape.shape( 'Red', 'Blue', 5)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_getstrokeColor(self):
        test_point = shape.shape('Red', 'Blue', 20)
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    
    def test_getfillColor(self):
        test_point = shape.shape('Red', 'Blue', 20)
        return self.assertEqual('Red', test_point.getfillColor())
    
    def test_setstrokeWidth(self): 
        test_point =  shape.shape('Red', 'Blue', 5)
        test_point.setstrokeWidth(5)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_setstrokeColor(self): 
        test_point = shape.shape('Red', 'Blue', 20)
        test_point.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    def test_setfillColor(self): 
        test_point = shape.shape('Red', 'Blue', 20)
        test_point.setfillColor('Red')
        return self.assertEqual('Red', test_point.getfillColor())
   
     #Shapes for the circle
     
    def test_getstrokeWidth2(self):
        test_point = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_getstrokeColor2(self):
        test_point = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    
    def test_getfillColor2(self):
        test_point = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual('Red', test_point.getfillColor())
    
    def test_setstrokeWidth2(self): 
        test_point =  cirlce.circle(20, points.Point(10, 45))
        test_point.setstrokeWidth(5)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_setstrokeColor2(self): 
        test_point = cirlce.circle(20, points.Point(10, 45))
        test_point.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    def test_setfillColor2(self): 
        test_point = cirlce.circle(20, points.Point(10, 45))
        test_point.setfillColor('Red')
        return self.assertEqual('Red', test_point.getfillColor())
    
    #Shapes for the rectangle
     
    def test_getstrokeWidth3(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_getstrokeColor3(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    
    def test_getfillColor3(self):
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual('Red', test_point.getfillColor())
    
    def test_setstrokeWidth3(self): 
        test_point =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.setstrokeWidth(5)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_setstrokeColor3(self): 
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    def test_setfillColor3(self): 
        test_point = rectangle.rectangle(20, 45, points.Point(15, 40))
        test_point.setfillColor('Red')
        return self.assertEqual('Red', test_point.getfillColor())
   
    
    #Shapes for the points
     
    def test_getstrokeWidth4(self):
        test_point = points.Point(15, 40)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_getstrokeColor4(self):
        test_point = points.Point(15, 40)
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    
    def test_getfillColor4(self):
        test_point = points.Point(15, 40)
        return self.assertEqual('Red', test_point.getfillColor())
    
    def test_setstrokeWidth4(self): 
        test_point =  points.Point(15, 40)
        test_point.setstrokeWidth(5)
        return self.assertEqual(5, test_point.getstrokeWidth())
    
    def test_setstrokeColor4(self): 
        test_point = points.Point(15, 40)
        test_point.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_point.getstrokeColor())
        
    def test_setfillColor4(self): 
        test_point = points.Point(15, 40)
        test_point.setfillColor('Red')
        return self.assertEqual('Red', test_point.getfillColor())

#Part 4.b      
if __name__ == '__main__': 
    unittest.main() 



