import tkinter.filedialog
import os
import numpy
import configparser
import shutil

from nptdms import TdmsFile

from InputData import InputData


class InputFinding:
    def parameterSearch(self,TDMSPath):
        config = configparser.ConfigParser()
        config.read('config.txt')
        #This section reads the needed information from the config file 
        startFreq = config.getint('Frequencies','Start Frequency')
        stopFreq = config.getint('Frequencies','Stop Frequency')
        stepFreq = config.getint('Frequencies','Step Frequency')
        NUM_POINTS = config.getint('Symbolic Constants','Num Points')
        JUMP_BACK = config.getint('Symbolic Constants','Jump Back')
        MIN_AMP =  config.getfloat('Symbolic Constants','Min Amp')
        
        TDMS_Time = []
        TDMS_Data = []
        TDMSfiles = os.listdir(TDMSPath)
        TDMSfiles = [file for file in TDMSfiles if file.endswith('.tdms')]
        for file in TDMSfiles: #Loop through all TDMS files in order to get the data within each
            path = TDMSPath + '/' + file
            TDMS = TdmsFile(path) #Function that reads the specific TDMS file
            group = TDMS.groups()[0]
            channel = TDMS.object(group, 'Dev1/ai0') #returns a channel type
            data = channel.data
            time = channel.time_track()
            
            #Determining starting point to read file
            #if highest point is more than JUMP_BACK points into the data, start there
            if numpy.argmax(data)>JUMP_BACK:
                start = numpy.argmax(data)-JUMP_BACK
            else: start = 0 #otherwise start at the beginning of the file

            t = time[start:start+NUM_POINTS]  #time information from the start point to the end point
            s = data[start:start+NUM_POINTS] #data from the start point to the end point
            '''
            Before I uncomment this segment I need to know what minimum threshold to detect, the one given in the email triggers for thousands of data points. I may be misinterpreting something. Felipe.
            for i in range(len(s)):
                if s[i] > MIN_AMP:
                    print('Warning: Index ' + str(i) +' of file ' + file + ' in Grade ' + TDMSPath.split('Grade')[1][1] + ' '  ' drops below the minimum voltage threshold')
            '''
            TDMS_Time.append(t) #add the TDMS files data to the set of all TDMS files data
            TDMS_Data.append(s)

        #Now that the data has all been found it can be set using the InputData() class

        InputData.Set_Start_Freq(startFreq)
        InputData.Set_Stop_Freq(stopFreq)
        InputData.Set_Step_Freq(stepFreq)
        InputData.Set_TDMS_Time(TDMS_Time)
        InputData.Set_TDMS_Data(TDMS_Data)
        
    def findGrades(self,directory):
        if not os.path.exists(directory + '/Analysis'):
            os.makedirs(directory + '/Analysis')
        else:   
            shutil.rmtree(directory + '/Analysis') #remove whole analysis folder if it exists
            os.makedirs(directory + '/Analysis')   #recreate analysis folder
        grades = os.listdir(directory)
        grades = [grade for grade in grades if (grade.count('.') == 0 and grade[:5].lower() == 'grade')] #Only analyze folders beginning with the word 'Grade'
        return grades
    def findExperiments(self,experimentPath):
        if len(os.listdir(experimentPath)) == 0:
            print('No folders to search found within ' + experimentPath)
        experiments = os.listdir(experimentPath) #list of experiments within each specific 'Grade' folder
        experiments = [experiment for experiment in experiments if (experiment.count('.') == 0 and not(experiment[:8].lower() == 'analysis' or experiment[:4].lower() == 'high'))] #leaves directories and anything not beginning in 'analysis' or '
        for i in range(len(experiments)):
            experiments[i] = experiments[i][0].upper() + experiments[i][1:]
        return experiments
    def findTests(self,testPath):
        if len(os.listdir(testPath)) == 0:
            print('No folders to search found within ' + testPath)
        tests = os.listdir(testPath)
        tests = [test for test in tests if test.count('.') == 0 and test[:4].lower() == 'test']
        return tests
    def findTDMS(self,TDMSPath):
        files = os.listdir(TDMSPath)
        files = [file for file in files if file.endswith(".tdms")]
        if len(files) == 0: #If there are no TDMS files skip directory
            print('No TDMS files found within ' + TDMSPath)
        return files
