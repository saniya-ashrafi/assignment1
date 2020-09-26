# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:53:56 2020

@author: DELL
"""

rows = 5
for i in range(2, rows):
    for j in range(1, i + 1):
        print("*", end=' ')
    print(" ")



for i in range(rows + 0, 1, - 2):
    for j in range(1, i - 1):
        print("*", end=' ')
    print(" ")