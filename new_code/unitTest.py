from InputFinding import InputFinding
from InputData import InputData
from PlotData import PlotData
from TransformedSignalData import TransformedSignalData
from FilteredData import FilterData
from Output import Output

import os
import filecmp
import unittest
import shutil
import numpy
import configparser

class UnitTest(unittest.TestCase):
    DataTests = [100,150.12,'String Test',[1,2,3],[[1,2,3],[4,5,6],[7,8,9]],[[1.1123,'2',3],[[4,5,6],'String Test',6],[9]]]

    def TestInputFinding(self):
        config = configparser.ConfigParser()
        config.read('config.txt')
        finding = InputFinding()
        path = 'standard_test_cases/input 1/Grade 0/experiment 1/test'
        finding.parameterSearch(path)
        
        assert InputData.Get_Start_Freq() == config.getint('Frequencies','Start Frequency'),'Starting Frequency is incorrect'
        assert InputData.Get_Stop_Freq() == config.getint('Frequencies','Stop Frequency'),'Stopping Frequency is incorrect'
        assert InputData.Get_Step_Freq() == config.getint('Frequencies','Step Frequency'),'Frequency Step is incorrect'
        assert len(InputData.Get_TDMS_Time()) == 10, 'TDMS Time does not have the proper number of entries'
        assert len(InputData.Get_TDMS_Data()) == 10, 'TDMS Data does not have the proper number of entries'

        #Somehow have to test the 2 major lists, unsure how at the moment. Testing length is not sufficient.
        #Additionally the Input Finding Module requests the user to input 3 values, unsure how to automate this

    def TestInputData(self):
        for test in self.DataTests:
            InputData.Set_Start_Freq(test)
            InputData.Set_Stop_Freq(test)
            InputData.Set_Step_Freq(test)
            InputData.Set_TDMS_Time(test)
            InputData.Set_TDMS_Data(test)
            assert InputData.Get_Start_Freq() == test, 'Starting Frequency is incorrect'
            assert InputData.Get_Stop_Freq() == test, 'Stopping Frequency is incorrect'
            assert InputData.Get_Step_Freq() == test, 'Step Frequency is incorrect'
            assert InputData.Get_TDMS_Time() == test, 'TDMS Data is incorrect'
            assert InputData.Get_TDMS_Data() == test, 'TDMS Time is incorrect'
        
                
    def setupPlotData(self):
        plotter = PlotData()
        path = 'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test'
        if not os.path.exists(path):
            os.makedirs(path+'/Event Pictures')
            os.makedirs(path+'/Contour Plot')
        else:
            shutil.rmtree(path)
            os.makedirs(path+'/Event Pictures')
            os.makedirs(path+'/Contour Plot')
        InputData.Set_Start_Freq(1)
        InputData.Set_Stop_Freq(2)
        InputData.Set_Step_Freq(1)
        InputData.Set_TDMS_Data(numpy.asarray([[1,2,3,4,5],[10,20,30,40,50]]))
        InputData.Set_TDMS_Time(numpy.asarray([[1,2,3,4,5],[100,200,300,400,500]]))
        TransformedSignalData.Set_Original_Transformed_Data(numpy.asarray([[2,4,6,8,10],[10,20,30,40,50]]))
        TransformedSignalData.Set_Original_Frequency_Data(numpy.asarray([[2,4,6,8,10],[10,20,30,40,50]]))
        plotter.plot(path)
    
    def TestPlotData(self):
        self.setupPlotData()
        assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/1kHz Original.png','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/1kHz Original.png'), '1kHz Original is incorrect'
        assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/2kHz Original.png','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/2kHz Original.png'), '2kHz Original is incorrect'
    '''    
    In order to give a set of plot tests I would need the "correct" plots to compare to. These were created with matplotlib manually, is this acceptable?
    Other than having something accurate to compare to this test should work fully.
    '''

    def TestTransformedSignalData(self):
        for test in self.DataTests:
            TransformedSignalData.Set_Original_Transformed_Data(test)
            TransformedSignalData.Set_Filtered_Transformed_Data(test)
            TransformedSignalData.Set_Original_Frequency_Data(test)
            TransformedSignalData.Set_Filtered_Frequency_Data(test)
            assert TransformedSignalData.Get_Original_Transformed_Data() == test, 'Original Transformed Data failed for test input: ' + str(test)
            assert TransformedSignalData.Get_Filtered_Transformed_Data() == test, 'Filtered Transformed Data failed for test input: ' + str(test)
            assert TransformedSignalData.Get_Original_Frequency_Data() == test, 'Original Frequency Data failed for test input: ' + str(test)
            assert TransformedSignalData.Get_Filtered_Frequency_Data() == test, 'Transformed Frequency Data failed for test input: ' + str(test)
            

    def TestFilteredData(self):
        for test in self.DataTests:
            FilterData.Set_Approximate_Coefficients(test)
            FilterData.Set_Detailed_Coefficients(test)
            assert FilterData.Get_Approximate_Coefficients() == test, 'Approximate Coefficients failed for test input: ' + str(test)
            assert FilterData.Get_Detailed_Coefficients() == test, 'Detailed Coefficients failed for test input: ' + str(test)

    def setupOutput(self):
        path = 'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test'
        InputData.Set_Start_Freq(1)
        InputData.Set_Stop_Freq(2)
        InputData.Set_Step_Freq(1)
        TransformedSignalData.Set_Original_Transformed_Data(numpy.asarray([[2,4,6,8,10],[3,6,9,12,15]]))
        TransformedSignalData.Set_Filtered_Transformed_Data(numpy.asarray([[1,2,3,4,5],[10,20,30,40,50]]))
        TransformedSignalData.Set_Original_Frequency_Data(numpy.asarray([[5,10,15,20,25],[4,8,12,16,20]]))
        TransformedSignalData.Set_Filtered_Frequency_Data(numpy.asarray([[6,12,18,24,30],[7,14,21,28,35]]))
        output = Output()
        output.output(path)

    def TestOutput(self):
        self.setupOutput()
        assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Filtered_Data.txt','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Filtered_Data.txt')
        assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Original_Data.txt','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Original_Data.txt')
        #assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Scattering_Data.txt','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Scattering_Data.txt')
        #I created these files thinking about what the answer should be in a separate python script, is this a suitable way to test?

#Creates a single test suite containing each test case
def suite():
        
    suite = unittest.TestSuite()
    suite.addTest(UnitTest("TestInputFinding"))
    suite.addTest(UnitTest("TestInputData"))
    suite.addTest(UnitTest("TestPlotData"))
    suite.addTest(UnitTest("TestTransformedSignalData"))
    suite.addTest(UnitTest("TestFilteredData"))
    suite.addTest(UnitTest("TestOutput"))
    return suite

#The following lines are for swift execution of the test cases
runner = unittest.TextTestRunner()
tester = suite()
runner.run(tester)
