from InputData import InputData
from TransformedSignalData import TransformedSignalData
import numpy ####Take out if testAmp is different from what is wanted

class Output():
    def output(self,path):
        start = InputData.Get_Start_Freq()
        stop = InputData.Get_Stop_Freq()
        step = InputData.Get_Step_Freq()
        
        originalData = TransformedSignalData.Get_Original_Transformed_Data()
        filterData = TransformedSignalData.Get_Filtered_Transformed_Data()
        originalFrequencyData = TransformedSignalData.Get_Original_Frequency_Data()
        filterFrequencyData = TransformedSignalData.Get_Filtered_Frequency_Data()
        
        testAmp = []
        '''Dont like these need to know why this is happening, will rename and redo after I understand'''
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
            for j in range(len(originalFrequencyData[i])): #Loop through data within the current TDMS file

                col1 = str((i*step)+start)
                
                col2 = str(originalFrequencyData[i][j])
                col2filtered = str(filterFrequencyData[i][j])

                col3 = str(testAmp[i][j])
                col3filtered = str(filterTestAmp[i][j])

                originalText.write(col1+','+col2+','+col3+'\n')
                filteredText.write(col1+','+col2filtered+','+col3filtered+'\n')

        '''
        The only thing remaining is the scattering factor which i dont really understand.
        I could copy it but I dont really want to.
        '''

        originalText.close()
        filteredText.close()
        scatteredText.close()
