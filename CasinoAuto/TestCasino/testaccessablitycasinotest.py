'''
Created on Aug 14, 2018

@author: Daryoush

'''

import unittest
import nose
import time

from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.HomePageM import HomePageM

class accessablitycasinotest(BaseTestCase,unittest.TestCase):


    def setUp(self):
        super(accessablitycasinotest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'])
        self.driver.maximize_window()
        time.sleep(2)
        # Verify A User Can Access Casino From Matchbook HomepageM using left hand nevigation
    def testlhnCasino(self):
        
        home_page_obj = HomePageM(self.driver)
        home_page_obj.lhn()
        time.sleep(10)#tester can see the red highlighted casino Icon
        # Verify A User Can Access Casino From Matchbook Homepage using top page casino Icon nevigation
    def testIcontopCasino(self):
        
        home_page_obj = HomePageM(self.driver)
        home_page_obj.top()
    def testIconliveCasinolhn(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.lhnlivecasino()
        print("Pass: Left hand navigation Icon live casino")
    def testIconliveCasino(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.livecasino()
        print("Icon live casino Daryoush")

    def testpromotionsCasino(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.promotions()
        time.sleep(2)

    def testpodcast(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.podcast()
        time.sleep(5)
    def testinsights(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.insights()
        time.sleep(5)

    def testappss(self):
        home_page_obj = HomePageM(self.driver)
        home_page_obj.apps()
        time.sleep(5)

    def tearDown(self):
        super(accessablitycasinotest, self).tearDown()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    nose.main()