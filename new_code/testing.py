import os
import filecmp
import sys
import unittest
import configparser

from PIL import Image
from PIL import ImageChops

from main import main
class SystemTestCase(unittest.TestCase):
    def testSetup(self):

        main()
        config = configparser.ConfigParser()
        config.read('config.txt')
        mainOutput = config['Paths']['Main Directory'] + '/Analysis/Grade 0/experiment 1/test'
        testOutput = 'standard_test_cases/input 1/Expected Output/Analysis/Grade 0/Experiment 1/test'


        if (os.listdir(mainOutput) != os.listdir(testOutput)):
            print('The two given directories do not contain the same text files and folders, the output is not the same.')
            sys.exit()
            
        comparisons = [] 
        comparisons.append(filecmp.cmp(mainOutput + '/Original_Data.txt',testOutput+ '/Original_Data.txt'))
        comparisons.append(filecmp.cmp(mainOutput + '/Filtered_Data.txt',testOutput+ '/Filtered_Data.txt'))
        #comparisons.append(filecmp.cmp(mainOutput + '/Scattering_Data.txt',testOutput+ '/Scattering_Data.txt'))
        #Right now this isnt done so commenting this out

        if (os.listdir(mainOutput +'/Event Pictures') != os.listdir(testOutput+'/Event Pictures')):
            print('The two given directories do not contain the same plots, the output is not the same.')
            sys.exit()
        newPlots = os.listdir(mainOutput + '/Event Pictures')
        oldPlots = os.listdir(testOutput + '/Event Pictures')
        for i in range(len(newPlots)):
            newImage = Image.open(mainOutput + '/Event Pictures/' + newPlots[i])
            oldImage = Image.open(testOutput + '/Event Pictures/' + oldPlots[i])
            diff = ImageChops.difference(newImage, oldImage)
            comparisons.append(diff.getbbox() == None)
          
        newPlots = os.listdir(mainOutput + '/Contour Plot')
        oldPlots = os.listdir(testOutput + '/Contour Plot')            
        newImage = Image.open(mainOutput + '/Contour Plot/' + newPlots[0])
        oldImage = Image.open(testOutput + '/Contour Plot/' + oldPlots[0])
        diff = ImageChops.difference(newImage, oldImage)
        comparisons.append(diff.getbbox() == None)
        
        return comparisons
        
    def systemTest(self):
        results = self.testSetup()
        for i in range(len(results)):
            assert results[i], 'Entry ' + str(i+1) +' failed the comparison'

runner = unittest.TextTestRunner()
test1 = SystemTestCase('systemTest')
runner.run(test1)
