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
        test_rect = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(15, test_rect.gettopLeftPoint().getX())
    
    def test_get_Width(self):
        test_rect  =  rectangle.rectangle(20,45, points.Point(15, 40))
        return self.assertEqual(20, test_rect.getWidth())   
    
    def test_get_Height(self):
        test_rect  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(45, test_rect.getHeight())    
    
    def test_set_top_Left_Point(self):
        test_rect  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_rect.settopLeftPoint(points.Point(10,45))
        return (self.assertEqual(10, test_rect.gettopLeftPoint().getX()) and self.assertEqual(45, test_rect.gettopLeftPoint().getY()))


    def test_set_Width(self):
        test_rect  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_rect.setWidth(20)
        return self.assertEqual(20, test_rect.getWidth())
    
    def test_set_Height(self):
        test_rect  =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_rect.setHeight(45)
        return self.assertEqual(45, test_rect.getHeight())
    
    def test_area_rect(self):
        test_rect = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(900, test_rect.area())
        
    def test_centroid(self):
        test_rect = rectangle.rectangle(20, 45, points.Point(15, 40))
        point= test_rect.centroid()
        return self.assertEqual(test_rect.gettopLeftPoint().getX()+ test_rect.getWidth()/2,point.getX()) and self.assertEqual(test_rect.gettopLeftPoint().getY()+ test_rect.getHeight()/2,point.getY())

        
    def test_contains_rect(self):
        test_rect = rectangle.rectangle(1, 1, points.Point(15, 40))
        return self.assertEqual(False, test_rect.contains(points.Point(-1,-1)))
        
    def test_perimeter_rect(self):
        test_rect= rectangle.rectangle(20,45, points.Point(10, 45))
        return self.assertEqual(130, test_rect.perimeter())

    
#Circle function 

    def test_get_center_Point(self):
        test_circle = cirlce.circle(20, points.Point(10, 45))
        return (self.assertEqual(10, test_circle.getcenterPoint().getX()) and self.assertEqual(45, test_circle.getcenterPoint().getY()))
    
    def test_get_radius(self):
        test_circle = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(20, test_circle.getradius())
    
    def test_set_center_Point(self):
        test_circle  =  cirlce.circle(20, points.Point(5, 4205))
        test_circle.setcenterPoint(points.Point(10,45))
        return (self.assertEqual(10, test_circle.getcenterPoint().getX()) and self.assertEqual(45, test_circle.getcenterPoint().getY()))
    
    def test_set_radius(self):
        test_circle  =  cirlce.circle(20, points.Point(10, 45))
        test_circle.setradius(20)
        return self.assertEqual(20, test_circle.getradius())
    
    def test_area_circle(self):
        test_circle = cirlce.circle(20, points.Point(15, 40))
        return self.assertEqual(math.pi*20**2,test_circle.area())
        
    def test_perimeter_cirlce(self):
        test_circle= cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(20*2*math.pi, test_circle.perimeter())
        
    def test_contains_circle(self):
        test_circle = cirlce.circle(2, points.Point(15, 40))
        return self.assertEqual(True, test_circle.contains(points.Point(16,41)))

          
   #Shapes for the original classes

    def test_getstrokeWidth(self):
        test_shape = shape.shape( 'Red', 'Blue', 5)
        return self.assertEqual(5, test_shape.getstrokeWidth())
    
    def test_getstrokeColor(self):
        test_shape = shape.shape('Red', 'Blue', 20)
        return self.assertEqual('Blue', test_shape.getstrokeColor())
        
    
    def test_getfillColor(self):
        test_shape = shape.shape('Red', 'Blue', 20)
        return self.assertEqual('Red', test_shape.getfillColor())
   #Demonstration of changed values. Please review
   
    def test_setstrokeWidth(self): 
        test_shape =  shape.shape('Red', 'Blue', 5)
        test_shape.setstrokeWidth(10)
        return self.assertEqual(10, test_shape.getstrokeWidth())
    
    def test_setstrokeColor(self): 
        test_shape = shape.shape('Red', 'Blue', 20)
        test_shape.setstrokeColor('Green')
        return self.assertEqual('Green', test_shape.getstrokeColor())
        
    def test_setfillColor(self): 
        test_shape = shape.shape('Red', 'Blue', 20)
        test_shape.setfillColor('Pink')
        return self.assertEqual('Pink', test_shape.getfillColor())
   
     #Shapes for the circle
     
    def test_getstrokeWidth2(self):
        test_shapecircle = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual(5, test_shapecircle.getstrokeWidth())
    
    def test_getstrokeColor2(self):
        test_shapecircle = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual('Blue', test_shapecircle.getstrokeColor())
        
    
    def test_getfillColor2(self):
        test_shapecircle = cirlce.circle(20, points.Point(10, 45))
        return self.assertEqual('Red', test_shapecircle.getfillColor())
    #Demonstration 2 for changed values
    def test_setstrokeWidth2(self): 
        test_shapecircle =  cirlce.circle(20, points.Point(10, 45))
        test_shapecircle.setstrokeWidth(5)
        return self.assertEqual(5, test_shapecircle.getstrokeWidth())
    
    def test_setstrokeColor2(self): 
        test_shapecircle = cirlce.circle(20, points.Point(10, 45))
        test_shapecircle.setstrokeColor('Grey')
        return self.assertEqual('Grey', test_shapecircle.getstrokeColor())
        
    def test_setfillColor2(self): 
        test_shapecircle = cirlce.circle(20, points.Point(10, 45))
        test_shapecircle.setfillColor('Lilac')
        return self.assertEqual('Lilac', test_shapecircle.getfillColor())
    
    #Shapes for the rectangle
     
    def test_getstrokeWidth3(self):
        test_shaperect = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual(5, test_shaperect.getstrokeWidth())
    
    def test_getstrokeColor3(self):
        test_shaperect = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual('Blue', test_shaperect.getstrokeColor())
        
    
    def test_getfillColor3(self):
        test_shaperect = rectangle.rectangle(20, 45, points.Point(15, 40))
        return self.assertEqual('Red', test_shaperect.getfillColor())
    
    def test_setstrokeWidth3(self): 
        test_shaperect =  rectangle.rectangle(20, 45, points.Point(15, 40))
        test_shaperect.setstrokeWidth(5)
        return self.assertEqual(5, test_shaperect.getstrokeWidth())
    
    def test_setstrokeColor3(self): 
        test_shaperect = rectangle.rectangle(20, 45, points.Point(15, 40))
        test_shaperect.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_shaperect.getstrokeColor())
        
    def test_setfillColor3(self): 
        test_shaperect = rectangle.rectangle(20, 45, points.Point(15, 40))
        test_shaperect.setfillColor('Red')
        return self.assertEqual('Red', test_shaperect.getfillColor())
   
    
    #Shapes for the points
     
    def test_getstrokeWidth4(self):
        test_shapepoint = points.Point(15, 40)
        return self.assertEqual(5, test_shapepoint.getstrokeWidth())
    
    def test_getstrokeColor4(self):
        test_shapepoint = points.Point(15, 40)
        return self.assertEqual('Blue', test_shapepoint.getstrokeColor())
        
    
    def test_getfillColor4(self):
        test_shapepoint = points.Point(15, 40)
        return self.assertEqual('Red', test_shapepoint.getfillColor())
    
    def test_setstrokeWidth4(self): 
        test_shapepoint =  points.Point(15, 40)
        test_shapepoint.setstrokeWidth(5)
        return self.assertEqual(5, test_shapepoint.getstrokeWidth())
    
    def test_setstrokeColor4(self): 
        test_shapepoint = points.Point(15, 40)
        test_shapepoint.setstrokeColor('Blue')
        return self.assertEqual('Blue', test_shapepoint.getstrokeColor())
        
    def test_setfillColor4(self): 
        test_shapepoint= points.Point(15, 40)
        test_shapepoint.setfillColor('Red')
        return self.assertEqual('Red', test_shapepoint.getfillColor())

#Part 4.b      
if __name__ == '__main__': 
    unittest.main() 



