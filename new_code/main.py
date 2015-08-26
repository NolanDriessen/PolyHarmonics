from tkinter import Tk
import tkinter.filedialog
import os
import time
import shutil
import configparser

from InputFinding import InputFinding
from Filtering import Filtering
from SignalTransform import SignalTransform
from PlotData import PlotData
from Output import Output


def main():
    #Read the main path from the config files
    config = configparser.ConfigParser()
    config.read('config.txt')
    directory = config['Paths']['Main Directory']

    #Initalize timer
    t0= time.time()

    grades = InputFinding().findGrades(directory) #Searches the path in the config file for all "Grade" folders
    for grade in grades:
        experimentPath = directory + '/' + grade #the path that leads to the experiment folders
        experiments = InputFinding().findExperiments(experimentPath) #Finds all "Experiment" folders
        for experiment in experiments:
            testPath = experimentPath + '/' + experiment #path leading to test folders
            tests = InputFinding().findTests(testPath) #Finds all "test" folders
            for test in tests:
                TDMSPath = testPath + '/' + test #path to the set of TDMS files
                InputFinding().findTDMS(TDMSPath)
                plotPath = directory + '/Analysis/' + grade + '/' + experiment + '/' + test   #The path used to store the plots produced by plotter
                os.makedirs(plotPath + '/Event Pictures') #Creates the required directories for storing the plots
                os.makedirs(plotPath + '/Contour Plot')
                InputFinding().parameterSearch(TDMSPath) #Uses the InputParams module to collect input for the system
                Filtering().Haar() #Takes the Haar wavelet filter
                SignalTransform().Transform() #Applies the FFT to both the filtered data and the original data
                PlotData().plot(plotPath)  #Creates the plots on both the original data and the transformed data
                Output().output(plotPath) #Creates the text files
                print('Done ' + grade +experiment + test)
    print('Elapsed Time: ' + ('%.2f' % (time.time() - t0)) + ' s')

if __name__ == "__main__":
    main()
