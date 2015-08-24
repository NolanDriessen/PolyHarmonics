##McMaster University - Chemical Engineering Department
##Acoustics Monitoring in Polymers Project
##Supervisor: Dr. Thompson
##Code programmed by Felipe Gomes and Trevor West
##May 2014
##
##Objective: Read a series of experiment files and generate a FFT plot for each test and
## a text file with all results for each emitted frequency.
##
import os
import sys
import shutil
import time
import numpy as npa
import matplotlib.pyplot as plt
import tkFileDialog
import scipy.ndimage
import pywt 
from Tkinter import Tk
from matplotlib.ticker import ScalarFormatter
from nptdms import TdmsFile

#Define options for opening or saving a file
Tk().withdraw()

StartFreq = input('Enter the Starting Frequency: ')
StopFreq = input('Enter the Stopping Frequency: ')
Gap = input('Enter the Frequency Step: ')

main = tkFileDialog.askdirectory(initialdir = 'C:/', title = 'Please select the file folder')

t0 = time.time() #Start timing the program.

grades = os.listdir(main)
grades = [grade for grade in grades if grade.count('.') == 0]
grades = [grade for grade in grades if grade[:5].lower() == 'grade']
grades = [main + "/" + grade for grade in grades]

#########Maiking Results Folder############
main += r'/' + 'Analysis'
if not os.path.exists(main): os.makedirs(main)
else:   
    shutil.rmtree(main)
    os.makedirs(main)
############################################ 
for grade in sorted(grades):

    modes = os.listdir(grade)
    modes = [mode for mode in modes if mode.count('.') == 0]
    modes = [mode for mode in modes if not(mode[:8].lower() == 'analysis' or mode[:4].lower() == 'high')]
    Grade = str(grade.split(' '))[-3]
    
    gmain = main + "/Grade " + str(Grade)
    if not os.path.exists(gmain): os.makedirs(gmain)

    ExCount = 0
    for experiment in sorted(modes):

        dirname = grade + "/" + experiment

        folders = os.listdir(dirname)
        folders = [folder for folder in folders if folder.count('.') == 0]
        folders = [folder for folder in folders if folder[:4].lower() == 'test']
        
        emain = gmain + "/Experiment " + str(ExCount + 1)
        if not os.path.exists(emain): os.makedirs(emain)
        
        textA = open(emain + r"/Original_Data.txt", "w")
        textB = open(emain + r"/Filtered_Data.txt", "w")
        textC = open(emain + r"/Scattering_Data.txt", "w")
    
        for folder in folders:
            trials = os.listdir(dirname + '/' + folder)
            trials = [trial for trial in trials if trial.endswith(".tdms")]


            events = os.listdir(dirname + '/' + folder)
            events = [event for event in events if event.endswith(".tdms")]

###########Stores each event data WITHIN the Experiment Folder####################
            Freq_Data  = []
            Amp_Data   = []

            Freq_Dataf = []
            Amp_Dataf  = []
##################################################################################
            EvCount = 0
            for event in sorted(events):

                #Reading TDMS File
                file  = TdmsFile(dirname + '/' + folder + '/' + event)
                gname = file.groups()[0]
                data = file.object(gname, 'Dev1/ai0')
                datatime = data.time_track()
                delta0 = 10000

                #Determining starting point to read file
                if npa.argmax(data.data)>4000: f0 = npa.argmax(data.data)-4000
                else: f0 = 0

                t = datatime[f0:f0+delta0]
                s = data.data[f0:f0+delta0]

                #Wavelet transform
                cA, cD = pywt.dwt(s, 'haar')

                t2 = map(lambda i: t[i],filter(lambda i: i%2 == 1,range(len(t))))

################FFT Transform on Filtered Data##########################
                n = len (cD)
                datafft = npa.fft.fft(cD, 5000)/n
                n = 5000
                datafft = datafft[0:n/2]
                time_step = ((t2[1]-t2[0])*1000)
                freq = npa.fft.fftfreq(n, time_step)
                freq = freq[0:n/2]

                Freq_Dataf = npa.append(Freq_Dataf, freq)
                Amp_Dataf  = npa.append(Amp_Dataf, abs(datafft)/max(abs(datafft)))
                                                               
################FFT Transform on Raw Data###############################
                n2 = len(s)
                datafft2 = npa.fft.fft(s, 10000)/n2
                n2 = 10000
                datafft2 = datafft2[0:n2/4]
                time_step2 = ((t[1]-t[0])*1000)
                freq2 = npa.fft.fftfreq(n2, time_step2)
                freq2 = freq2[0:n2/4]

                Freq_Data = npa.append(Freq_Data, freq2)
                Amp_Data  = npa.append(Amp_Data, abs(datafft2)/max(abs(datafft2)))

############################Ploting Figures##############################
                PicsPath = emain + "/Event Pictures"
                if not os.path.exists(PicsPath): os.makedirs(PicsPath)

                fig = plt.figure()
                plt.subplots_adjust(left=0.25, bottom=0.25)
                x_formatter = ScalarFormatter(useOffset=False)

                ax1 = fig.add_subplot(2,1,1)
                ax1.set_ylim(min(s)-0.1*min(s), max(s)+0.1*max(s))
                ax1.xaxis.set_major_formatter(x_formatter)
                l, = plt.plot(t,s, lw=1, color='blue')
                plt.xlabel('Time(s)')
                plt.ylabel('Amplitude')

                ax3 = fig.add_subplot(2,1,2)
                ax3.set_ylim(0, max(abs(datafft2))+0.1*max(abs(datafft2)))
                ax3.xaxis.set_major_formatter(x_formatter)
                l2, = plt.plot(freq2,abs(datafft2), lw=2, color='green')
                plt.xlabel('Freq (kHz)')
                plt.ylabel('Amplitude')
                axcolor = 'lightgoldenrodyellow'

                plt.tight_layout()

                plt.savefig(PicsPath + '/' +  str((EvCount*Gap)+StartFreq) + 'kHz Original' + '.png', bbox_inches = 'tight')

                plt.close('all')


########################Writing Text Files################################
                CurrentFreq = (EvCount*Gap)+ StartFreq    ##Add calculation about scattering
                FirstSide = 0
                SecondSide = 0
                MainSignal = 0
                PeakRange = 5
                DeltaFreq = Freq_Data[1]-Freq_Data[0]
                
                for l in range(0 + EvCount*len(freq), len(Freq_Data)):

                    line0 = str((EvCount*Gap)+ StartFreq)
                    
                    line1  = str(Freq_Data[l])
                    line1a = str(Freq_Dataf[l])
                    
                    line2  = str(Amp_Data[l])
                    line2a = str(Amp_Dataf[l])

                    if Freq_Data[l]<CurrentFreq-PeakRange: FirstSide=FirstSide+(Amp_Data[l]*DeltaFreq)
                    if Freq_Data[l]>CurrentFreq+PeakRange: SecondSide=SecondSide+(Amp_Data[l]*DeltaFreq)
                    if abs(Freq_Data[l]-CurrentFreq)<PeakRange: MainSignal = MainSignal+(Amp_Data[l]*DeltaFreq)

                    textA.write(line0+","+line1+","+line2+"\n")
                    textB.write(line0+","+line1a+","+line2a+"\n")
                    l+=1
                    
                l = 0                   
                EvCount +=1

                ScFactorMain = 1-(MainSignal/(FirstSide+SecondSide+MainSignal))
                ScFactorSide1 =FirstSide/(FirstSide+SecondSide+MainSignal)
                ScFactorSide2 =SecondSide/(FirstSide+SecondSide+MainSignal)
                textC.write(str(CurrentFreq)+","+str(ScFactorMain)+","+str(ScFactorSide1)+","+str(ScFactorSide2)+"\n")

############################Contour Plotting##############################
            ConPath = emain +r"/Contour Plot"
            if not os.path.exists(ConPath): os.makedirs(ConPath)

            Ef = npa.arange(StartFreq, StopFreq + 40, Gap)
            Xm = npa.empty([10, 2500])
            for i in range(0, len(Ef)):
                Xm[i][0:] = Ef[i]

            Ym = npa.reshape(Freq_Data, (10, 2500))
            Zm = npa.reshape(Amp_Data, (10, 2500))
                    
            Xm = scipy.ndimage.zoom(Xm, 3)
            Ym = scipy.ndimage.zoom(Ym, 3)
            Zm = scipy.ndimage.zoom(Zm, 3)

            plt.contourf(Xm, Ym, abs(Zm))
            plt.xlabel('Emitted Frequency [kHz]')
            plt.ylabel('Recorded Frequency [kHz]')
            plt.colorbar().set_label('Amplitude [V]')

            plt.tight_layout()

            plt.savefig(ConPath +'/' + experiment + '.png', bbox_inches = 'tight')
            plt.close('all')

        ExCount += 1
        
        textA.close()
        textB.close()
        textC.close()

    print "Grade " + str(Grade) + " is complete!"
          
print 'Elapsed Time: ' + ('%.2f' % (time.time() - t0)) + ' s'
