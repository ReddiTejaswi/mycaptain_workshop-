# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:47:22 2021

@author: Dell
"""
import math;

r=float(input("Radius of cicle: "))
      
print("area of cicle with radius ", r, " is:" ,(math.pi*r**2))

dict={"py":"python","c":"C","html":"hHTML","java":"Java"}

filename=input("Input the filename: ")
#for taking the extension of file
s=filename.split(".");
print("The extension of the file is : {}".format(dict.get(s[1])))
