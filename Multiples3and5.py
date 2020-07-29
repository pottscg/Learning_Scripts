#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:53:42 2020

@author: catherine

Project_Euler -- pottscg_123
Euler1254

Sums multiples of 3 and 5 found between 1 and 1000
"""

sum = 0

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum+i;

print(sum)
