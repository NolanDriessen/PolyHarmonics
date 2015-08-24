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

#class Main():
def main():
    #Initalize classes
    finder = InputFinding()
    haar = Filtering()
    transformer = SignalTransform()
    plotter = PlotData()
    output = Output()

    #Read the main path from the config files
    config = configparser.ConfigParser()
    config.read('config.txt')
    directory = config['Paths']['Main Directory']

    #Initalize timer
    t0= time.time()

    grades = finder.findGrades(directory) #Searches the path in the config file for all "Grade" folders
    for grade in grades:
        experimentPath = directory + '/' + grade #the path that leads to the experiment folders
        experiments = finder.findExperiments(experimentPath) #Finds all "Experiment" folders
        for experiment in experiments:
            testPath = experimentPath + '/' + experiment #path leading to test folders
            tests = finder.findTests(testPath) #Finds all "test" folders
            for test in tests:
                TDMSPath = testPath + '/' + test #path to the set of TDMS files
                finder.findTDMS(TDMSPath)
                plotPath = directory + '/Analysis/' + grade + '/' + experiment + '/' + test   #The path used to store the plots produced by plotter
                os.makedirs(plotPath + '/Event Pictures') #Creates the required directories for storing the plots
                os.makedirs(plotPath + '/Contour Plot')
                finder.parameterSearch(TDMSPath) #Uses the InputParams module to collect input for the system
                haar.Haar() #Takes the Haar wavelet filter
                transformer.Transform() #Applies the FFT to both the filtered data and the original data
                plotter.plot(plotPath)  #Creates the plots on both the original data and the transformed data
                output.output(plotPath)

    print('Elapsed Time: ' + ('%.2f' % (time.time() - t0)) + ' s')

if __name__ == "__main__":
    main()
