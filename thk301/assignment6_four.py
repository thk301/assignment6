# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  assignment6.py 
#  March 31,2015
#
#  various numpy exercises
#
###################################


import numpy as np
import matplotlib.pyplot as plt

class SixFour:
  # Problem 4 A
  def __init__(self, a,b,c,d,N_max, some_threshold):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.N_max = N_max
        self.some_threshold = some_threshold


  def numberFour(self,a,b,c,d,N_max, some_threshold):
    """
    Write a module that computes the Mandelbrot fractal using the Mandelbrot iteration
    """
    x,y= np.ogrid[a:b:200j,c:d:200j]  #Constructing a grid of ​c = x + 1j*y​values in the range ​[­2, 1] x [­1.5, 1.5]
  
    c = x + 1j*y                 #code given
    z=c
    for v in xrange(N_max):     #Do the iteration
         z = z**2 + c               # this gives  RuntimeWarning: overflow encountered in square.  
                                    # sent TA an email to ask.  He replied that the value exceeding the capacity of an int
    if np.abs(z).all() < some_threshold:    #A point ​(x,y)​belongs to the Mandelbrot set if ​abs(z) < some_threshold
        mask = np.abs(z) 
        return mask
    else:
        pass
    
 


  




