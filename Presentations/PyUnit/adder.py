import unittest

class MathTestCase(unittest.TestCase):
    ##unittest.TestCase
##
##    def setUp (self):
##        print("Setting up test cases")
##
##    def tearDown (self):
##        print("Cleaning up test cases")
    
##  the setUp method is called before every test, while the tearDown method is called after everytest
##  for such a simple example these were not needed but they can be very useful!  


    def adder(self,x,y):
        c = x+y
        return c

    def TestAdder(self):
        self.failUnless (self.adder(1,8)==9, '1 + 8 != 9!')
        self.failIf(self.adder(16,765)!= 781)
        assert self.adder(3,2) == 5, 'math went wrong'

    def subber(self,x,y):
        c = x-y
        return c

    def TestSubber(self):
        self.failUnless (self.subber(9,2)==7, '9-2 != 7!')
        self.failIf(self.subber(1753,1920)!= -167)
        assert self.subber(5,2) == 3, 'math went wrong'

    def mather(self,a,b,x,y):
        add = self.adder(a,b)
        sub = self.subber(x,y)
        return add+sub

    def TestMather(self):
        self.failUnless (self.mather(42,13,21,17)==59, '4+3 + 2-1 != 8!')
        assert self.mather(4,3,2,1) == 8, 'math went wrong'

        #####THIS ONE FAILS####
        self.failIf(15 != 12, 'clearly 15 isnt 12 so this fails!')



def suite():
        
    suite = unittest.TestSuite()
    suite.addTest(MathTestCase("TestAdder"))
    suite.addTest(MathTestCase("TestSubber"))
    suite.addTest(MathTestCase("TestMather"))
    
    return suite

