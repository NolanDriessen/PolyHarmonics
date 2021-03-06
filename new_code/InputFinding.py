from __future__ import absolute_import
import tkFileDialog, FileDialog
import os
import numpy
import ConfigParser
import shutil
import sys

from nptdms import TdmsFile

from InputData import InputData


class InputFinding(object):
    def parameterSearch(self,TDMSPath):
        config = ConfigParser.ConfigParser()
        config.read(u'config.txt')
        
        #This section reads the needed information from the config file 
        startFreq = config.getint(u'Frequencies',u'Start Frequency')
        stopFreq = config.getint(u'Frequencies',u'Stop Frequency')
        stepFreq = config.getint(u'Frequencies',u'Step Frequency')
        NUM_POINTS = config.getint(u'Symbolic Constants',u'Num Points')
        JUMP_BACK = config.getint(u'Symbolic Constants',u'Jump Back')
        
        TDMS_Time = []
        TDMS_Data = []
        TDMSfiles = os.listdir(TDMSPath)
        TDMSfiles = [file for file in TDMSfiles if file.endswith(u'.tdms')]
        for file in TDMSfiles: #Loop through all TDMS files in order to get the data within each
            path = TDMSPath + u'/' + file
            TDMS = TdmsFile(path) #Function that reads the specific TDMS file
            group = TDMS.groups()[0]
            channel = TDMS.object(group, u'Dev1/ai0') #returns a channel type
            data = channel.data
            time = channel.time_track()
            
            #Determining starting point to read file
            #if highest point is more than JUMP_BACK points into the data, start there
            if numpy.argmax(data)>JUMP_BACK:
                start = numpy.argmax(data)-JUMP_BACK
            else: start = 0 #otherwise start at the beginning of the file

            t = time[start:start+NUM_POINTS]  #time information from the start point to the end point
            s = data[start:start+NUM_POINTS] #data from the start point to the end point

            TDMS_Time.append(t) #add the TDMS files data to the set of all TDMS files data
            TDMS_Data.append(s)

        #Now that the data has all been found it can be set using the InputData class

        InputData.Set_Start_Freq(startFreq)
        InputData.Set_Stop_Freq(stopFreq)
        InputData.Set_Step_Freq(stepFreq)
        InputData.Set_TDMS_Time(TDMS_Time)
        InputData.Set_TDMS_Data(TDMS_Data)
        
    def findGrades(self,directory):
        
        if not os.path.exists(directory + u'/Analysis'):
            os.makedirs(directory + u'/Analysis')
        else:   
            shutil.rmtree(directory + u'/Analysis') #remove whole analysis folder if it exists
            os.makedirs(directory + u'/Analysis')   #recreate analysis folder
        grades = os.listdir(directory)
        grades = [grade for grade in grades if (grade.count(u'.') == 0 and grade[:5].lower() == u'grade')] #Only analyze folders beginning with the word 'Grade'
        if len(grades) == 0:
            print u'No folders to search found within ' + directory
            print u'Please modify config.txt to contain the folder to search'
        return grades
    def findExperiments(self,experimentPath):
        experiments = os.listdir(experimentPath) #list of experiments within each specific 'Grade' folder
        experiments = [experiment for experiment in experiments if (experiment.count(u'.') == 0 and not(experiment[:8].lower() == u'analysis' or experiment[:4].lower() == u'high'))] #leaves directories and anything not beginning in 'analysis' or '
        for i in xrange(len(experiments)):
            experiments[i] = experiments[i][0].upper() + experiments[i][1:]
        if len(experiments) == 0:
            print u'No folders to search found within ' + experimentPath
            print u'Please modify config.txt to contain the folder to search'
        return experiments
    def findTests(self,testPath):
        tests = os.listdir(testPath)
        tests = [test for test in tests if test.count(u'.') == 0 and test[:4].lower() == u'test']
        if len(tests) == 0:
            print u'No folders to search found within ' + testPath
            print u'Please modify config.txt to contain the folder to search'
        return tests
    def findTDMS(self,TDMSPath):
        files = os.listdir(TDMSPath)
        files = [file for file in files if file.endswith(u".tdms")]
        if len(files) == 0: #If there are no TDMS files skip directory
            print u'No TDMS files found within ' + TDMSPath
            print u'Please modify config.txt to contain the folder to search'
        return files
