from InputData import InputData
from TransformedSignalData import TransformedSignalData
import numpy
class Output():
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
        originalText = open(path + '/Original_Data.txt', 'w')
        filteredText = open(path + '/Filtered_Data.txt', 'w')
        scatteredText = open(path + '/Scattering_Data.txt', 'w')
        
        for i in range(len(filterData)): #Loop through TDMS files
            CurrentFreq = (i*step)+start
            DeltaFreq = originalFrequencyData[i][1]-originalFrequencyData[i][0]
            for j in range(len(originalFrequencyData[i])): #Loop through data within the current TDMS file

                col1 = str(CurrentFreq)
                
                col2 = str(originalFrequencyData[i][j])
                col2filtered = str(filterFrequencyData[i][j])

                col3 = str(testAmp[i][j])
                col3filtered = str(filterTestAmp[i][j])

                originalText.write(col1+','+col2+','+col3+'\n')
                filteredText.write(col1+','+col2filtered+','+col3filtered+'\n')
                if originalFrequencyData[i][j]<(CurrentFreq-PeakRange): FirstSide=FirstSide+(testAmp[i][j]*DeltaFreq) 
                if originalFrequencyData[i][j]>(CurrentFreq+PeakRange): SecondSide=SecondSide+(testAmp[i][j]*DeltaFreq)
                if abs(originalFrequencyData[i][j]-CurrentFreq)<PeakRange: MainSignal = MainSignal+(testAmp[i][j]*DeltaFreq)
            #print("Main Signal: " + str(MainSignal)+ " First Side " + str(FirstSide) + " Second Side " + str(SecondSide))
            ScFactorMain = 1-(MainSignal/(FirstSide+SecondSide+MainSignal))
            ScFactorSide1 =FirstSide/(FirstSide+SecondSide+MainSignal)
            ScFactorSide2 =SecondSide/(FirstSide+SecondSide+MainSignal)
            scatteredText.write(str((i*step)+start)+","+str(ScFactorMain)+","+str(ScFactorSide1)+","+str(ScFactorSide2)+"\n")
        '''
        The only thing remaining is the scattering factor which i dont really understand.
        I could copy it but I dont really want to.
        '''

        originalText.close()
        filteredText.close()
        scatteredText.close()
