import os
import csv
import math
import numpy as np
import pandas as pd
import Libs.Weibull as WB
import Libs.PathLenghtDistribution as PLD

def RPP_CREME(IRPP_LET_Spectra, IRPP_Component, LETth):
    LET_values=IRPP_LET_Spectra.index
    IRPP_WB_Parameters=IRPP_Component.GetWeibullParametersHI()
    XSection_lim=IRPP_WB_Parameters[0]
    a=IRPP_Component.GetA()*0.0001 #thickness -> um to cm
    b=IRPP_Component.GetB()*0.0001
    c=IRPP_Component.GetC()*0.0001
    w=IRPP_Component.GetW()*0.0001
    A=2*(a*b+b*c+a*c)*0.0001#um2 -> m2
    DSI=2.321
    Qc=LETth*a*0.1032845
    Energy=22.5*Qc
    a=a*DSI
    b=b*DSI
    c=c*DSI
    Pmax=math.sqrt(a**2+b**2+c**2)    
    Lmin=Energy/Pmax
    Q=Lmin
    LETminBinI=(np.abs(LET_values - Lmin)).argmin()
    Sum=0.
    for i in range(LETminBinI, len(LET_values)):
        Li=LET_values[i]
        F=IRPP_LET_Spectra.iloc[i,0]*10000/(4*math.pi)
        D=Energy/Li
        Sum+=(Li-Q)*PLD.DifferentialPLD_val(D, a, b, c)*F/(Li**2)
        Q=Li
    return Energy*A*math.pi*Sum


def IRPP_CREME(IRPP_LET_Spectra, IRPP_Component):
    IRPPComponentParameter=IRPP_Component.GetWeibullParametersHI()
    LETrange=IRPP_LET_Spectra.index
    LETminBin=(np.abs(LETrange - IRPPComponentParameter[1])).argmin()
    WB1=WB.GetWeibullXsection(IRPPComponentParameter, LETrange[LETminBin])
    TotalRate=0.
    for LETbin in range(LETminBin, len(LETrange)):
        rate=RPP_CREME(IRPP_LET_Spectra, IRPP_Component, LETrange[LETbin])
        WB2=WB.GetWeibullXsection(IRPPComponentParameter, LETrange[LETbin])
        thisRate=rate*abs(WB2-WB1)
        TotalRate+=thisRate
        WB1=WB2
    TotalRate=TotalRate/IRPPComponentParameter[0]
    return TotalRate






