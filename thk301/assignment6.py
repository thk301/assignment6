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
import assignment6_one as a6one
import assignment6_two as a6two
import assignment6_three as a6three
from assignment6_four import SixFour


def separator():  
    """
    Separate between answers for easy readability 
    """
    print ""
    print "*"*25
    print ""
    return None

def answerOne(a,b,c):    # create array by calling addNum
    """
    prints out assignment6_one: various numpy exercises
    """   
    thisArray, oneA, oneB, oneC, oneD = a6one.numberOne(a,b,c)
    separator()
    print "Array to be used for problem 1."
    print thisArray                         
    separator()
    
    # Problem 1 A  - Generate a new array containing the 2nd and 4th rows
    print "Answer 1a"
    print oneA
    separator()

    # Problem 1 B  - Generate a new array that contains the 2nd column
    print "Answer 1b"
    print oneB
    separator()
 
    # Problem 1 C - Generate a new array that contains all the elements in the rectangular 
    #                 section between the coordinates ​[1,0]​and ​[3,2]
    print "Answer 1c"
    print oneC
    separator()
 
    # Problem 1 D - Generate a new array that contains only elements with values that are between 3 and 11
    print "Answer 1d"
    print sorted(thisArray[oneD])    #sorted incrementally

def answerTwo(a,b,c):
    """
    prints out assignment6_two: divides each column element­wise with the array
    """
    print "Answer 2"
    print a6two.numberTwo(a,b,c)
    
    
def answerThree(a,b):
    printer, threeAList, printerC, threeCList = a6three.numberThree(a,b)
      #Problem 3 A  - For each row, pick the number closest to 0.5
    print "Answer 3a"  
    for item in printer:
        print item
    print ""
    print "1­D array--->", threeAList  #1D array of the numbers from each row closes to 0.5
    separator()    

    # Problem 3 B and 3 C
    print "Answer 3b and 3c"
    for item in printerC:
        print item
    print ""
    print "1­D array--->", threeCList
    return threeAList,threeCList


def answerFour(a,b,c,d,e,f):
    result = SixFour(a,b,c,d,e,f)
    mask = result.numberFour(a,b,c,d,e,f)
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')           #Save the result to an image 
    
if __name__ == "__main__":
    answerOne(1,6,11)
    separator()
    answerTwo(25,5,5)
    separator()
    answerThree(10,3)
    separator()
    answerFour(-2, 1, -1.5, 1.5, 50, 50)


