'''
Created on Feb06 , 2019

@author: Daryoush
'''
import unittest
import nose
#import time
from AdminAuto.Pages.BaseTestCase import BaseTestCase
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Pages.HomePageM import HomePageM

class admintabstest(BaseTestCase,unittest.TestCase):


    def setUp(self):
        super(admintabstest, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testavailabletabs(self):
        element = HomePageM(self.driver)
        element.clickAdminstration()

    def tearDown(self):
            super(admintabstest, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()