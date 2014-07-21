#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to get the entire and decimal part of a float data in Python?

¿Cómo obtener la parte entera y decimal de un dato float en Python?
'''

import math

#create a float number
f = 126.7364
print(f)

#this method generates a tuple with two floats, the first is the decimal part
#and the second is the integer part. Both items carry the sign of 'f'.
t = math.modf(f)
print(type(t))
print(t)

#create a negative number
f = -25.2763
print(f)

#return the both parts.
t = math.modf(f)
print(t)
