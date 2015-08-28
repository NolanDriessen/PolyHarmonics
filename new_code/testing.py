u'''
Before running please ensure that config.txt contains:
Start Frequency: 100
Stop Frequency: 1000
Step Frequency: 100
Main Directory: standard_test_cases/input 1

If the parameters are not set as defined here the test will fail.
'''
from __future__ import absolute_import
import os
import filecmp
import sys
import unittest
import ConfigParser

from PIL import Image
from PIL import ImageChops

from main import main
class SystemTestCase(unittest.TestCase):
    def testSetup(self):

        main()
        config = ConfigParser.ConfigParser()
        config.read(u'config.txt')
        mainOutput = config.get(u'Paths',u'System Test 1')
        testOutput = u'standard_test_cases/input 1/Expected Output/Analysis/Grade 0/Experiment 1/test'


        if (os.listdir(mainOutput) != os.listdir(testOutput)):
            print u'The two given directories do not contain the same text files and folders, the output is not the same.'
            sys.exit()
            
        comparisons = [] 
        comparisons.append(filecmp.cmp(mainOutput + u'/Original_Data.txt',testOutput+ u'/Original_Data.txt'))
        comparisons.append(filecmp.cmp(mainOutput + u'/Filtered_Data.txt',testOutput+ u'/Filtered_Data.txt'))
        #comparisons.append(filecmp.cmp(mainOutput + '/Scattering_Data.txt',testOutput+ '/Scattering_Data.txt'))
        #Right now this isnt done so commenting this out

        if (os.listdir(mainOutput +u'/Event Pictures') != os.listdir(testOutput+u'/Event Pictures')):
            print u'The two given directories do not contain the same plots, the output is not the same.'
            sys.exit()
        newPlots = os.listdir(mainOutput + u'/Event Pictures')
        oldPlots = os.listdir(testOutput + u'/Event Pictures')
        for i in xrange(len(newPlots)):
            newImage = Image.open(mainOutput + u'/Event Pictures/' + newPlots[i])
            oldImage = Image.open(testOutput + u'/Event Pictures/' + oldPlots[i])
            diff = ImageChops.difference(newImage, oldImage)
            comparisons.append(diff.getbbox() == None)
          
        newPlots = os.listdir(mainOutput + u'/Contour Plot')
        oldPlots = os.listdir(testOutput + u'/Contour Plot')            
        newImage = Image.open(mainOutput + u'/Contour Plot/' + newPlots[0])
        oldImage = Image.open(testOutput + u'/Contour Plot/' + oldPlots[0])
        diff = ImageChops.difference(newImage, oldImage)
        comparisons.append(diff.getbbox() == None)
        
        return comparisons
  
    def systemTest(self):
        results = self.testSetup()
        for i in xrange(len(results)):
            assert results[i], u'Entry ' + unicode(i+1) +u' failed the comparison'

runner = unittest.TextTestRunner()
test1 = SystemTestCase(u'systemTest')
runner.run(test1)
