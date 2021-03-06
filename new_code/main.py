from __future__ import absolute_import
from Tkinter import Tk
import tkFileDialog, FileDialog
import os
import time
import shutil
import ConfigParser

from InputFinding import InputFinding
from Filtering import Filtering
from SignalTransform import SignalTransform
from PlotData import PlotData
from Output import Output


def main():
    #Read the main path from the config files
    config = ConfigParser.ConfigParser()
    config.read(u'config.txt')
    directory = config.get(u'Paths',u'Main Directory')

    #Initalize timer
    t0= time.time()

    grades = InputFinding().findGrades(directory) #Searches the path in the config file for all "Grade" folders
    for grade in grades:
        experimentPath = directory + u'/' + grade #the path that leads to the experiment folders
        experiments = InputFinding().findExperiments(experimentPath) #Finds all "Experiment" folders
        for experiment in experiments:
            testPath = experimentPath + u'/' + experiment #path leading to test folders
            tests = InputFinding().findTests(testPath) #Finds all "test" folders
            for test in tests:
                TDMSPath = testPath + u'/' + test #path to the set of TDMS files
                InputFinding().findTDMS(TDMSPath)
                plotPath = directory + u'/Analysis/' + grade + u'/' + experiment + u'/' + test   #The path used to store the plots produced by plotter
                os.makedirs(plotPath + u'/Event Pictures') #Creates the required directories for storing the plots
                os.makedirs(plotPath + u'/Contour Plot')
                InputFinding().parameterSearch(TDMSPath) #Uses the InputParams module to collect input for the system
                Filtering().Haar() #Takes the Haar wavelet filter
                SignalTransform().Transform() #Applies the FFT to both the filtered data and the original data
                PlotData().plot(plotPath)  #Creates the plots on both the original data and the transformed data
                Output().output(plotPath) #Creates the text files
                print u'Done ' + grade + u' ' + experiment + u' ' + test
    print u'Elapsed Time: ' + (u'%.2f' % (time.time() - t0)) + u' s'

if __name__ == u"__main__":
    main()
