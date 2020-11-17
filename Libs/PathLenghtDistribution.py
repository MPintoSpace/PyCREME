import sys
import os.path
import csv
import math
import numpy as np
import pandas as pd
import statistics
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
from dateutil.relativedelta import relativedelta
from mpmath import mp
mp.prec = 108
mp.dps = 30

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)

#def Component(L, W, H):
#    print(L, W, H)
    
def DifferentialPLD_val(dS, dL, dW, dH):
    AP=3.*(dH*dW+dH*dL+dL*dW)
    G1=G(dS, dL, dW, dH)
    G2=G(dS, dW, dL, dH)
    G3=G(dS, dL, dH, dW)
    G4=G(dS, dW, dH, dL)
    G5=G(dS, dH, dW, dL)
    G6=G(dS, dH, dL, dW)
    result=(G1+G2+G3+G4+G5+G6)/(math.pi*AP)
    return result

def G(gS, gX, gY, gZ):
    KSQ=gX*gX+gY*gY
    TSQ=gX*gX+gZ*gZ
    T=math.sqrt(TSQ)
    RSQ=KSQ+gZ*gZ
    R=math.sqrt(RSQ)
    V=12.*gX*gY*gZ*gZ
    PSQ=gS*gS-gZ*gZ
    QSQ=gS*gS-gX*gX-gZ*gZ

    if ((gS>=0.0) &(gS<gZ)):
        return ( (8.*gY*gY*gZ/KSQ) -(gS*((3.*gX*gY/(R*T))**2)) )

    elif ((gS>=gZ) & (gS<T)):
        return gS*((3.*gY/math.sqrt(KSQ))**2) -gS*((3.*gX*gY/(T*R))**2) -gX*(math.sqrt(PSQ)/gS)*(8.+4.*gZ*gZ/(gS*gS)) +((V*math.atan(gY/gX)-((gY*gZ*gZ/math.sqrt(KSQ))**2))/(gS*gS*gS))

    elif ((gS>=T) & (gS<R)):
        return (-gS*((3.*gX*gZ/(R*math.sqrt(KSQ)))**2) +(gX*gX*gZ*gZ*(gZ*gZ/KSQ -3.) +V*math.atan(gY/gX))/(gS*gS*gS)
        +gY*gZ*gZ*(math.sqrt(QSQ)/gS)*((8./TSQ)+(4./(gS*gS))) -((V/(gS*gS*gS))*math.acos(gX/math.sqrt(PSQ))))
    return 0.0
        
def DifferentialPLD(a, b, c, nbins):
    lenght_array=[]
    DiffPLD_array=[]
    maxL=math.sqrt(a**2+b**2+c**2)
    for i in range(0, nbins):
        l = maxL*i/nbins
        lenght_array.append(l)
        Diff_val=DifferentialPLD_val(l, c, b, a)
        DiffPLD_array.append(Diff_val)
    return lenght_array, DiffPLD_array

def IntegralPLD(a, b, c, nbins):
    larray, Diff = DifferentialPLD(a, b, c, nbins)
    IntPLD_array=np.zeros(nbins)
    Diff_sum=0.
    for i in range (0, nbins):
        Diff_sum+=Diff[nbins-i-1]
        IntPLD_array[nbins-i-1]=Diff_sum
    return larray, IntPLD_array/Diff_sum
