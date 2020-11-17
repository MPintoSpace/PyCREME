import os
import csv
import math
import numpy as np

def GetWeibullXsection(fWBfunctionParameters, fLET_value):
    if (fLET_value < fWBfunctionParameters[1]):
        return 0
    else:
        return np.float64(fWBfunctionParameters[0]*np.float64(((1-math.exp(np.float64(-(((fLET_value-fWBfunctionParameters[1])/fWBfunctionParameters[2])**fWBfunctionParameters[3])))))))
