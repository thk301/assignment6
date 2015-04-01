# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  unittest6.py 
#  March 31,2015
#
#  1. testing array is correctly built
#  2. testing listMaker returns correct list
#  3. testing values of problem 3 are equal
#
###################################

import unittest
import assignment6 as a6
import assignment6_one as a6one
import assignment6_two as a6two
import assignment6_three as a6three
import assignment6_four as a6four


class Assignment6Test(unittest.TestCase):

    def setUp(self):
        print "setUp"
    
    def testArray(self):
       self.assertEqual(a6one.addNum(1,6,11),  [[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
    
    def testListmaker(self):
        self.assertEqual(a6three.listMaker(1, 0.5, 0.1), [0.5, 0.0, 0.4])
    
    def testThree(self):
        printer, threeAList, printerC, threeCList = a6three.numberThree(10,3)  #compares two results of problem 3: 
                                           # one uses argmin that finds index of the smallest number
                                           # the other used argsort to sort by its value and gives the index
        self.assertEqual(threeAList, threeCList)
    

if __name__ == '__main__':
   unittest.main()
   
   