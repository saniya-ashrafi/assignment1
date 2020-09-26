# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:50:16 2020

@author: DELL
"""

def getMiddleThreeChars(sampStr):
  middleIndex = int(len(sampStr) /2)
  
  middleThree = sampStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are", middleThree)
  

getMiddleThreeChars("Jasonay")