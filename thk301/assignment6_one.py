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


def addNum(one, two, three):    
    """
    Create 2-D array 5 rows of 3 (one, two, three) numbers - increment of 1
    """
    numList=[]
    for item in xrange(5):
        addThis=[one+item,two+item, three+item]          #increment of 1
        numList.append(addThis)
    return numList                            


def numberOne(one, two, three):
    """
    various numpy exercises
    """   
    
    # create array by calling addNum
    thisArray = np.array(addNum(one, two, three))   #thisArray will be used for number 1 question
    
    # Problem 1 A  - Generate a new array containing the 2nd and 4th rows
    oneA = thisArray[np.array([1,3])]

    # Problem 1 B  - Generate a new array that contains the 2nd column
    oneB = thisArray[:, 1]
 
    # Problem 1 C - Generate a new array that contains all the elements in the rectangular 
    #                 section between the coordinates ​[1,0]​and ​[3,2]
    oneC = thisArray[1:4, 0:3]

    # Problem 1 D - Generate a new array that contains only elements with values that are between 3 and 11
    oneD = np.where((3<=thisArray[:]) & (thisArray[:]<=11))  #oneC will store index of values that are between 3 and 11

    return thisArray, oneA, oneB, oneC, oneD


