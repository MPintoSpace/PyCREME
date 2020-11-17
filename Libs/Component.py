import os
import csv
import math
import numpy as np
import pandas as pd

#Lenghts in um
#LET in MeVcm2/g
class Component():
    def __init__(self, ComponentName="SEU Monitor", thickness=1, sideY=3.87, sideZ=3.87,
                 fWeibullHI=[1.50E-07, 1200, 6500, 1.47], fWeibullProtons=[3.53E-14, 3.48E-02, 6.91E-02, 1]):
        self.__name=ComponentName
        self.__a=thickness
        self.__b=sideY
        self.__c=sideZ
        self.__WeibullParametersHI=fWeibullHI
        self.__WeibullParametersProtons=fWeibullProtons
        self.ComputeGeometricVariables()
        
    def ComputeGeometricVariables(self):
        self.__V=self.__a*self.__b*self.__c
        self.__S=2*(self.__b*self.__c+self.__c*self.__a+self.__a*self.__b)
        self.__y=6*self.__V*math.pi
        self.__z=self.__a+self.__b+self.__c
        self.__r=(self.__b**2)*(self.__c**2)+(self.__c**2)*(self.__a**2)+(self.__a**2)*(self.__b**2)
        self.__w=math.sqrt((self.__a**2)+(self.__b**2)+(self.__c**2))
        self.__mew_a=math.sqrt((self.__b**2)+(self.__c**2))
        self.__mew_b=math.sqrt((self.__a**2)+(self.__c**2))
        self.__mew_c=math.sqrt((self.__b**2)+(self.__a**2))
        self.__x0=max(self.__c,self.__mew_c)

    def PrintGeometricProperties(self):
        print("a", self.__a)
        print("b", self.__b)
        print("c", self.__c)
        print("V", self.__V)
        print("S", self.__S)
        print("y", self.__y)
        print("z", self.__z)
        print("r", self.__r)
        print("w", self.__w)
        print("mew_a", self.__mew_a)
        print("mew_b", self.__mew_b)
        print("mew_c", self.__mew_c)
        print("x0", self.__x0)

    def PrintWeibullParametersHI(self):
        print (__name+" Heavy Ion Weibull ")
        print ("Plataeu:", self.__WeibullParametersHI[0] ,"cm2/bit")
        print ("LET Threshold:", self.__WeibullParametersHI[1] ,"MeV.cm2/mg")
        print ("Width:", self.__WeibullParametersHI[2] ,"MeV.cm2/mg")
        print ("Shape Factor:", self.__WeibullParametersHI[3] ,"")

    def PrintWeibullParametersProtons(self):
        print (__name+" Proton Weibull Parameters")
        print ("Plataeu:", self.__WeibullParametersProtons[0] ,"cm2/bit")
        print ("LET Threshold:", self.__WeibullParametersProtons[1] ,"MeV")
        print ("Width:", self.__WeibullParametersProtons[2] ,"MeV")
        print ("Shape Factor:", self.__WeibullParametersProtons[3] ,"")
        
    def GetA(self):
        return self.__a

    def GetB(self):
        return self.__b

    def GetC(self):
        return self.__c
    
    def GetS(self):
        return self.__S

    def GetW(self):
        return self.__w
    
    def GetGeometricalProperties(self):
        return (self.__a, self.__b, self.__c)

    def GetWeibullParametersHI(self):
        return self.__WeibullParametersHI

    def GetWeibullParametersProtons(self):
        return self.__WeibullParametersProtons



def LoadComponent(LC_Name='SEU_Monitor'):
    #SEU
    SEU_Monitor_Geo=[2, 3.87298, 3.87298]
    SEU_Monitor_parameters_HI=[1.50E-07, 1200, 6500, 1.47]
    SEU_Monitor_parameters_Protons=[3.53E-14, 10, 4, 1]

    #SEL
    BS62_Geo=[1, 0.7169379331573968, 0.7169379331573968]    
    BS62_parameters_HI=[5.14E-09, 1., 3.52, 2.26] #SEU
    BS62_parameters_Protons=[2.64E-07, 10, 86.8, 2.04] #SEU
    
    BS62_Geo=[1, 7007.139217, 7007.139217] #SEL
    BS62_parameters_HI=[4.91E-01, 1000., 14500, 2.8] #SEL
    BS62_parameters_Protons=[2.64E-07, 10, 86.8, 2.04] #SEL

    K6R4_Geo=[1, 2886.173938, 2886.173938]
    K6R4_parameters_HI=[8.33E-02, 5000., 29400, 65]
    K6R4_parameters_Protons=[5.19E-10, 152, 55.5, 6.13]

    IS61_Geo=[1, 4898.979486, 4898.979486]
    IS61_parameters_HI=[2.40E-01, 1000., 16900, 4.]
    IS61_parameters_Protons=[3.03E-08, 5., 116.1, 2.09]

    IS62_Geo=[1, 4795.831523, 4795.831523]
    IS62_parameters_HI=[2.30E-01, 1900, 27500, 5.15]
    IS62_parameters_Protons=[2.70E-09, 60., 88.5, 1.92]
    
    if (LC_Name=='SEU_Monitor'):
        return Component(LC_Name, SEU_Monitor_Geo[0], SEU_Monitor_Geo[1], SEU_Monitor_Geo[2], SEU_Monitor_parameters_HI, SEU_Monitor_parameters_Protons)
    elif (LC_Name=='BS62'):
        return Component(LC_Name, BS62_Geo[0], BS62_Geo[1], BS62_Geo[2], BS62_parameters_HI, BS62_parameters_Protons)
    elif (LC_Name=='K6R4'):
        return Component(LC_Name, K6R4_Geo[0], K6R4_Geo[1], K6R4_Geo[2], K6R4_parameters_HI, K6R4_parameters_Protons)
    elif (LC_Name=='IS61'):
        return Component(LC_Name, IS61_Geo[0], IS61_Geo[1], IS61_Geo[2], IS61_parameters_HI, IS61_parameters_Protons)
    elif (LC_Name=='IS62'):
        return Component(LC_Name, IS62_Geo[0], IS62_Geo[1], IS62_Geo[2], IS62_parameters_HI, IS62_parameters_Protons)
