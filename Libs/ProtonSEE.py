import os
import csv
import math
import numpy as np
import pandas as pd
import Libs.Weibull as WB

def ComputeProtonSEErate(CPSR_Spectra, CPSR_Component):
    CPSR_SEErate=0.
    for i in range (0, len(CPSR_Spectra)-1):
        CPSR_deltaE=CPSR_Spectra.index[i+1]-CPSR_Spectra.index[i]
        CPSR_bin_flux=(CPSR_Spectra.iloc[i,0]+CPSR_Spectra.iloc[i+1,0])/2.
        CPSR_bin_energy=(CPSR_Spectra.index[i]+CPSR_Spectra.index[i+1])/2.
        CPSR_SEErate+=CPSR_bin_flux*WB.GetWeibullXsection(CPSR_Component.GetWeibullParametersProtons(),CPSR_bin_energy)*CPSR_deltaE
    return CPSR_SEErate #SEE rate/second
    
