from __future__ import absolute_import
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
import ConfigParser

class UnitTest(unittest.TestCase):
    DataTests = [100,150.12,u'String Test',[1,2,3],[[1,2,3],[4,5,6],[7,8,9]],[[1.1123,u'2',3],[[4,5,6],u'String Test',6],[9]]]

    def TestInputFinding(self):
        config = ConfigParser.ConfigParser()
        config.read(u'config.txt')
        finding = InputFinding()
        path = u'standard_test_cases/input 1/Grade 0/experiment 1/test'
        finding.parameterSearch(path)
        
        assert InputData.Get_Start_Freq() == config.getint(u'Frequencies',u'Start Frequency'),u'Starting Frequency is incorrect'
        assert InputData.Get_Stop_Freq() == config.getint(u'Frequencies',u'Stop Frequency'),u'Stopping Frequency is incorrect'
        assert InputData.Get_Step_Freq() == config.getint(u'Frequencies',u'Step Frequency'),u'Frequency Step is incorrect'
        assert len(InputData.Get_TDMS_Time()) == 10, u'TDMS Time does not have the proper number of entries'
        assert len(InputData.Get_TDMS_Data()) == 10, u'TDMS Data does not have the proper number of entries'

        #Somehow have to test the 2 major lists, unsure how at the moment. Testing length is not sufficient.
        #Additionally the Input Finding Module requests the user to input 3 values, unsure how to automate this

    def TestInputData(self):
        for test in self.DataTests:
            InputData.Set_Start_Freq(test)
            InputData.Set_Stop_Freq(test)
            InputData.Set_Step_Freq(test)
            InputData.Set_TDMS_Time(test)
            InputData.Set_TDMS_Data(test)
            assert InputData.Get_Start_Freq() == test, u'Starting Frequency is incorrect'
            assert InputData.Get_Stop_Freq() == test, u'Stopping Frequency is incorrect'
            assert InputData.Get_Step_Freq() == test, u'Step Frequency is incorrect'
            assert InputData.Get_TDMS_Time() == test, u'TDMS Data is incorrect'
            assert InputData.Get_TDMS_Data() == test, u'TDMS Time is incorrect'
        
                
    def setupPlotData(self):
        plotter = PlotData()
        path = u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test'
        if not os.path.exists(path):
            os.makedirs(path+u'/Event Pictures')
            os.makedirs(path+u'/Contour Plot')
        else:
            shutil.rmtree(path)
            os.makedirs(path+u'/Event Pictures')
            os.makedirs(path+u'/Contour Plot')
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
        assert filecmp.cmp(u'standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/1kHz Original.png',u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/1kHz Original.png'), u'1kHz Original is incorrect'
        assert filecmp.cmp(u'standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/2kHz Original.png',u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Event Pictures/2kHz Original.png'), u'2kHz Original is incorrect'
    u'''    
    In order to give a set of plot tests I would need the "correct" plots to compare to. These were created with matplotlib manually, is this acceptable?
    Other than having something accurate to compare to this test should work fully.
    '''

    def TestTransformedSignalData(self):
        for test in self.DataTests:
            TransformedSignalData.Set_Original_Transformed_Data(test)
            TransformedSignalData.Set_Filtered_Transformed_Data(test)
            TransformedSignalData.Set_Original_Frequency_Data(test)
            TransformedSignalData.Set_Filtered_Frequency_Data(test)
            assert TransformedSignalData.Get_Original_Transformed_Data() == test, u'Original Transformed Data failed for test input: ' + unicode(test)
            assert TransformedSignalData.Get_Filtered_Transformed_Data() == test, u'Filtered Transformed Data failed for test input: ' + unicode(test)
            assert TransformedSignalData.Get_Original_Frequency_Data() == test, u'Original Frequency Data failed for test input: ' + unicode(test)
            assert TransformedSignalData.Get_Filtered_Frequency_Data() == test, u'Transformed Frequency Data failed for test input: ' + unicode(test)
            

    def TestFilteredData(self):
        for test in self.DataTests:
            FilterData.Set_Approximate_Coefficients(test)
            FilterData.Set_Detailed_Coefficients(test)
            assert FilterData.Get_Approximate_Coefficients() == test, u'Approximate Coefficients failed for test input: ' + unicode(test)
            assert FilterData.Get_Detailed_Coefficients() == test, u'Detailed Coefficients failed for test input: ' + unicode(test)

    def setupOutput(self):
        path = u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test'
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
        assert filecmp.cmp(u'standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Filtered_Data.txt',u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Filtered_Data.txt')
        assert filecmp.cmp(u'standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Original_Data.txt',u'standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Original_Data.txt')
        #assert filecmp.cmp('standard_test_cases/Unit Testing/Expected Output/Analysis/Grade 0/Experiment 1/test/Scattering_Data.txt','standard_test_cases/Unit Testing/Unit Test Output/Analysis/Grade 0/Experiment 1/test/Scattering_Data.txt')
        
#Creates a single test suite containing each test case
def suite():
        
    suite = unittest.TestSuite()
    suite.addTest(UnitTest(u"TestInputFinding"))
    suite.addTest(UnitTest(u"TestInputData"))
    suite.addTest(UnitTest(u"TestPlotData"))
    suite.addTest(UnitTest(u"TestTransformedSignalData"))
    suite.addTest(UnitTest(u"TestFilteredData"))
    suite.addTest(UnitTest(u"TestOutput"))
    return suite

#The following lines are for swift execution of the test cases
runner = unittest.TextTestRunner()
tester = suite()
runner.run(tester)
