'''
Created on September 07, 2018

@author: Daryoush
'''

import unittest
import nose
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.CasinoPage import CasinoPage


class casinotlogintest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(casinotlogintest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    # Verify user name can log in
    def testLoginTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.click_logintop_button()


    def tearDown(self):
        super(casinotlogintest, self).tearDown()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    nose.main()