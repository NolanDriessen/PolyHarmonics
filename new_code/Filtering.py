import pywt

from InputData import InputData
from FilteredData import FilterData

#from FilterFormat import FilterData
class Filtering():
    def Haar(self):
        TDMSdata = InputData.Get_TDMS_Data()
        approx = [] #Holds the set of approximate coefficients
        detailed = [] #Holds the set of detailed coefficients
        '''This loop does the haar wavelet filter on the data found in each TDMS file:
        cA holds the approximate coefficients of the data found within the current for loop iteration
        cD holds the detailed coefficients of the data found within the current for loop iteration.'''
        for data in TDMSdata:
            cA, cD = pywt.dwt(data, 'haar')
            approx.append(cA)
            detailed.append(cD)

        #With the data from the haar wavelet we store it within the FilterData class
        FilterData.Set_Approximate_Coefficients(approx)
        FilterData.Set_Detailed_Coefficients(detailed)
