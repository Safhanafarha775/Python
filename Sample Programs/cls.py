# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:16:39 2023

@author: DELL
"""

class Circle:
    
    from math import pi
    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
          

    # Method for resetting Radius
    def setRadius(self):
        self.radius=float(input())
        self.area = self.radius * self.radius * self.pi
        print(locals())
        return self.area
        
    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
