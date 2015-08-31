from __future__ import division
from __future__ import absolute_import
from InputData import InputData
from TransformedSignalData import TransformedSignalData
import numpy
from io import open
class Output(object):
    def output(self,path):
        #Gets required input from classes.
        start = InputData.Get_Start_Freq()
        stop = InputData.Get_Stop_Freq()
        step = InputData.Get_Step_Freq()
        
        originalData = TransformedSignalData.Get_Original_Transformed_Data()
        filterData = TransformedSignalData.Get_Filtered_Transformed_Data()
        originalFrequencyData = TransformedSignalData.Get_Original_Frequency_Data()
        filterFrequencyData = TransformedSignalData.Get_Filtered_Frequency_Data()


        #Setting up variables for Scattered_Data.txt. This is created purely based off of PolyHarmonics-June2nd.py
        #***This creates different values than I was given
        FirstSide = 0 
        SecondSide = 0
        MainSignal = 0
        PeakRange = 5
        
        
        #Removes imaginary components and normalizes data
        testAmp = []
        for data in originalData:
            testAmp.append(abs(data)/max(abs(data)))
        filterTestAmp = []
        for data in filterData:
            filterTestAmp.append(abs(data)/max(abs(data)))

        #opens the three text files written by this module
        originalText = open(path + u'/Original_Data.txt', u'w')
        filteredText = open(path + u'/Filtered_Data.txt', u'w')
        scatteredText = open(path + u'/Scattering_Data.txt', u'w')
        
        for i in xrange(len(filterData)): #Loop through TDMS files
            CurrentFreq = (i*step)+start
            DeltaFreq = originalFrequencyData[i][1]-originalFrequencyData[i][0]
            for j in xrange(len(originalFrequencyData[i])): #Loop through data within the current TDMS file

                col1 = unicode(CurrentFreq)
                
                col2 = unicode(originalFrequencyData[i][j])
                col2filtered = unicode(filterFrequencyData[i][j])

                col3 = unicode(testAmp[i][j])
                col3filtered = unicode(filterTestAmp[i][j])

                originalText.write(col1+u','+col2+u','+col3+u'\n')
                filteredText.write(col1+u','+col2filtered+u','+col3filtered+u'\n')                
                if originalFrequencyData[i][j]<CurrentFreq-PeakRange: FirstSide=FirstSide+(testAmp[i][j]*DeltaFreq) 
                if originalFrequencyData[i][j]>CurrentFreq+PeakRange: SecondSide=SecondSide+(testAmp[i][j]*DeltaFreq)
                if abs(originalFrequencyData[i][j]-CurrentFreq)<PeakRange: MainSignal = MainSignal+(testAmp[i][j]*DeltaFreq)
            
            ScFactorMain = 1-(MainSignal/(FirstSide+SecondSide+MainSignal))
            ScFactorSide1 =FirstSide/(FirstSide+SecondSide+MainSignal)
            ScFactorSide2 =SecondSide/(FirstSide+SecondSide+MainSignal)
            scatteredText.write(unicode(CurrentFreq)+u","+unicode(ScFactorMain)+u","+unicode(ScFactorSide1)+u","+unicode(ScFactorSide2)+u"\n")


        originalText.close()
        filteredText.close()
        scatteredText.close()
