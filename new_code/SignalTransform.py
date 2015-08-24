import numpy
import configparser

from FilteredData import FilterData
from InputData import InputData
from TransformedSignalData import TransformedSignalData


class SignalTransform():
    def Transform(self):
        TDMSdata = InputData.Get_TDMS_Data()
        TDMStime = InputData.Get_TDMS_Time()
        filterData = FilterData.Get_Detailed_Coefficients()
        
        config = configparser.ConfigParser()
        config.read('config.txt')
        NUM_POINTS = config.getint('Symbolic Constants','Num Points')

        #The following for loop takes the FFT on the original data
        originalTransformData = []
        for data in TDMSdata:
            n = len(data)
            transform = numpy.fft.fft(data,NUM_POINTS)/n #Takes the FFT and normalizes it
            transform = transform[0:NUM_POINTS/4]
            originalTransformData.append(transform)

        #The following for loop takes the FFT on the filtered data
        filterTransformData = []
        for data in filterData:
            n = len(data)
            filterTransform = numpy.fft.fft(data,int(NUM_POINTS/2))/n
            filterTransform = filterTransform[0:NUM_POINTS/4]
            filterTransformData.append(filterTransform)
            
        originalFreqData = []
        filterFreqData = []
        for time in TDMStime:
            t2 = [time[i] for i in [i for i in range(len(time)) if i%2 == 1]]
            filterStep = ((t2[1]-t2[0])*1000)
            originalStep = ((time[1]-time[0])*1000)

            freqOriginal = numpy.fft.fftfreq(NUM_POINTS,originalStep)
            freqOriginal = freqOriginal[0:NUM_POINTS/4]
            originalFreqData.append(freqOriginal)

            freqFilter = numpy.fft.fftfreq(int(NUM_POINTS/2),filterStep)
            freqFilter = freqFilter[0:NUM_POINTS/4]
            filterFreqData.append(freqFilter)

        TransformedSignalData.Set_Original_Transformed_Data(originalTransformData)
        TransformedSignalData.Set_Filtered_Transformed_Data(filterTransformData)
        TransformedSignalData.Set_Original_Frequency_Data(originalFreqData)
        TransformedSignalData.Set_Filtered_Frequency_Data(filterFreqData)
