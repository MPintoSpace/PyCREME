import os
import csv
import numpy as np
import pandas as pd

def LoadLETspectra(path):
    fLET_spectra = pd.read_csv(path, sep=";")
    fLET=fLET_spectra['LET']
    fLET_spectra=fLET_spectra.set_index(fLET)
    return fLET_spectra.drop(columns=['LET'])

def LoadEnergySpectra(path):
    fEnergy_spectra = pd.read_csv(path, sep=";")
    fEnergy=fEnergy_spectra['Energy']
    fEnergy_spectra=fEnergy_spectra.set_index(fEnergy)
    return fEnergy_spectra.drop(columns=['Energy'])

