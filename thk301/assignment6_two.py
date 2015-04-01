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



def numberTwo(one, two, three):   
    """
    divides each column element­wise with the array
    """
    thisArrayTwo = np.arange(one).reshape(two, three)      #array one=25, two=5, three=5
    division = np.array([1., 5, 10, 15, 20])
    divisionT = np.array(division)[np.newaxis].T         #transpose to divides each column element­wise with the array
    resultTwo = np.divide(thisArrayTwo,divisionT)        #divide  
    return resultTwo


