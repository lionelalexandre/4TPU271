#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:19:34 2023

@author: lioneltruflandier
"""
from numpy import sqrt

def my_norm(v):
    res = 0.0
    for i in range(len(v)):
        res = res + v[i]**2
    # or
    #return sqrt(sum(b**2))
    return sqrt(res)

def my_inner(v,w):
    res = 0.0
    for i in range(len(v)):
        res = res + v[i]*w[i]
    return res
