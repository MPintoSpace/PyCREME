import os
import csv
import math
import numpy as np
import pandas as pd
import Libs.Component as Component
import Libs.Spectra as Spectra
import Libs.CREME as CREME
import Libs.ProtonSEE as ProtonSEE

print("Hello")    
component_name='K6R4'
#EEEcomponent = Component.Component("Example", 1, 10, 10, [1.6e-07
EEEcomponent = Component.LoadComponent(component_name) #Modificar
ComponentParameter=EEEcomponent.GetWeibullParametersHI()

#Spectra must have at least two columns LET (MeVcm2/g);IntegralFlux (#/cm2/s)
LET_Spectra=Spectra.LoadLETspectra("D:\TDP8\CTTB\Data_analysis\SEErate/MTB_HeU.csv")
Energy_Spectra=Spectra.LoadEnergySpectra("D:\TDP8\CTTB\Data_analysis\SEErate/Protons.csv")

UHeavyIons=CREME.IRPP_CREME(LET_Spectra, EEEcomponent)
print("Heavy Ions")
print("SEE/day", UHeavyIons*84600)

UProtons=ProtonSEE.ComputeProtonSEErate(Energy_Spectra, EEEcomponent)
print("Protons")
print("SEE/day", UProtons*84600)
