#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:00:39 2020

@author: catherine

Calculate the sum of the even Fibbonaci numbers that are smaller than 4million
"""

sum = 0

fib1 = 1
fib2 = 1

fib_next = fib1+fib2

while fib_next < 4000000:
    if fib_next % 2 == 0:
        sum = sum + fib_next
    
    fib1 = fib2
    fib2 = fib_next
    
    fib_next = fib1+fib2
    
print(sum)
