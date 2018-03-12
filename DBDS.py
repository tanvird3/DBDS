# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:15:58 2018

@author: KHAN
"""
import pandas as pd
import numpy as np
import math
import scipy as sc

# this function calculates the required interest rate for doubling any amount in any 
# given period
## n is the given time in year and c is the compounding frequency in a year
def doublebenefit(n,c):
    ip=c*(math.exp(math.log(2)/(n*c))-1)
    return ip

# this function calculates the interest rate per period based on the calculated interest
# rate from doublebenefit function
def intperp(n,c):
    ipp=(1+doublebenefit(n,c)/c)**(c/12)-1
    return ipp
    
doublebenefit(6,12)

intperp(6,12)

# checking the future value
def future_value(amt, n, c):
    ftv=np.fv(rate=intperp(n,c), pmt=0, nper=n*12, pv=-amt, when=1)
    return ftv

future_value(100000, 6, 12)
