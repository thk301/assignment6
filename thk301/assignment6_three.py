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



def listMaker(one, two, three):
    """
     receives three values and return a list after abs and -5
    """
    oneABS = abs(one-0.5)     #absolute value of the first value - 0.5
    twoABS = abs(two-0.5)      #absolute value of the second value - 0.5
    threeABS = abs(three-0.5)     #absolute value of the third value - 0.5
    tempList=[oneABS, twoABS, threeABS]          #store three into tempList
    return tempList


def numberThree(a,b):
    """
    generate a 10 x 3 array of random numbers in the range
    """
    
    threeArray = np.random.rand(a,b)    #a=10, b =3
    
    #Problem 3 A  - For each row, pick the number closest to 0.5
    threeAList=[]
    printer=[]
    for item in threeArray:
        thisIndex = np.argmin(listMaker(item[0],item[1],item[2]))         #used argmin to find index of the lowest value
        threeAList.append(item[thisIndex])         #add value into list
        thisString ="%s is the closest to 0.5 out of %s" %(item[thisIndex],item)
        printer.append(thisString)     #these are random values  

    # Problem 3 B and 3 C
    threeCList=[]
    printerC=[]
    for line in threeArray:
        thisIndex = np.argsort(listMaker(line[0],line[1],line[2]))            #np.argsort sorts the tempList by its value
        columnIndex = thisIndex[0]
        thisStringC= "Column %s has the closest to 0.5 out of %s" %(int(columnIndex), line)
        threeCList.append(line[columnIndex])
        printerC.append(thisStringC)
    return printer, threeAList, printerC, threeCList

