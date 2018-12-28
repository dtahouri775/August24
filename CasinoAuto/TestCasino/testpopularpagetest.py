'''
Created on November 23, 2018

@author: Daryoush
'''
import unittest
import nose
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Pages.PopularPage import PopularGamePage
from CasinoAuto.Constants import Casino_Constants

class popularpagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(popularpagetest, self).setUp()
        #self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def testsegration(self):
        segration = PopularGamePage(self.driver)
        result=segration .verifysegration()
    ''''
    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
       livegame = PopularGamePage(self.driver)
       result=livegame.verifylandingpageinfo(1)
    '''
    def tearDown(self):
        super(popularpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()