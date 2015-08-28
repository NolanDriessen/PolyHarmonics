import matplotlib.pyplot
import matplotlib.ticker
import numpy
import scipy.ndimage

from InputData import InputData
from TransformedSignalData import TransformedSignalData


class PlotData():
    def plot(self,path):
        #This segment acquires all required variables from their classes
        start = InputData.Get_Start_Freq()
        stop = InputData.Get_Stop_Freq()
        step = InputData.Get_Step_Freq()
        TDMSdata = InputData.Get_TDMS_Data()
        TDMStime = InputData.Get_TDMS_Time()
        originalTransform = TransformedSignalData.Get_Original_Transformed_Data()
        originalFrequency = TransformedSignalData.Get_Original_Frequency_Data()

        #Remove the imaginary components and normalize the data
        testFFT = []
        for data in originalTransform:
            testFFT.append(abs(data)/max(abs(data)))

        #Loop through each TDMS file and create the plots
        for i in range(len(TDMSdata)):
            fig = matplotlib.pyplot.figure()
            x_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False) #creates formatter for ticks on X axis
            matplotlib.pyplot.subplots_adjust(left=0.25, bottom=0.25)
        
            plot1 = fig.add_subplot(2,1,1) #Creates a 2x1 grid for first subplot
            plot1.set_ylim(0.9*min(TDMSdata[i]), 1.1*max(TDMSdata[i])) #Sets data limit for the y axis
            plot1.xaxis.set_major_formatter(x_formatter)
            originalFig = matplotlib.pyplot.plot(TDMStime[i],TDMSdata[i],color='blue') #Creates the plot
            matplotlib.pyplot.xlabel('Time(s)') #Labels axes
            matplotlib.pyplot.ylabel('Amplitude')
            
            plot2 = fig.add_subplot(2,1,2) #Creates a 2x1 grid for second subplot
            plot2.set_ylim(0, max(abs(originalTransform[i]))+0.1*max(abs(originalTransform[i])))  #Sets data limit for the y axis
            plot2.xaxis.set_major_formatter(x_formatter)
            transformedFig = matplotlib.pyplot.plot(originalFrequency[i],abs(originalTransform[i]), lw=2, color='green') #Creates the plot
            matplotlib.pyplot.xlabel('Freq (kHz)') #Labels axes
            matplotlib.pyplot.ylabel('Amplitude')
            axcolor = 'lightgoldenrodyellow'
            
            matplotlib.pyplot.tight_layout() #automatically adjusts subplots so that they fit into the figure area. 

            matplotlib.pyplot.savefig(path + '/Event Pictures/' + str((i*step)+start) + 'kHz Original' + '.png', bbox_inches = 'tight') #Saves the figure in the location specified

            matplotlib.pyplot.close('all') #Closes all figure windows

        #Contour plotting
        interval = numpy.arange(start, stop + 1, step) #Create a numpy array containing values spaced by step on the interval start to stop. The +1 forces the half closed interval to include the final value, the stopping frequency.
        Xm = numpy.empty([len(originalFrequency), len(originalFrequency[i])]) #Create a 2D numpy array without initializing values. 10 arrays of size 2500 each for the standard case
        for i in range(0, len(interval)): #Fills the array previously created
            Xm[i][0:] = interval[i]
        Ym = numpy.reshape(originalFrequency, (len(originalFrequency), -1))
        Zm = numpy.reshape(testFFT, (len(testFFT), -1))
                
        Xm = scipy.ndimage.zoom(Xm, 3) #Resampled by a factor of 3 with cubic interpolation
        Ym = scipy.ndimage.zoom(Ym, 3)
        Zm = scipy.ndimage.zoom(Zm, 3)

        matplotlib.pyplot.contourf(Xm, Ym, abs(Zm)) #Create the contour plot and fill it
        matplotlib.pyplot.xlabel('Emitted Frequency [kHz]') #Labels axes
        matplotlib.pyplot.ylabel('Recorded Frequency [kHz]')
        matplotlib.pyplot.colorbar().set_label('Amplitude [V]') #Labels the colour bar

        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.savefig(path + '/Contour Plot/' + path[path.find('Experiment'):path.find('Experiment')+12] + '.png', bbox_inches = 'tight')
        matplotlib.pyplot.close('all')

