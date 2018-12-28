'''
Created on December 10, 2018

@author: Daryoush
'''

import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.LiveCasinoPage import LiveCasinoPageM


class accessablitylivecasinotest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(accessablitylivecasinotest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'])
        self.driver.maximize_window()

        time.sleep(2)

        # Verify all options in live casino can be displayed and are clickable

    def testliveCasino(self):
        lc_page_obj = LiveCasinoPageM(self.driver)
        lc_page_obj.livelobbymenu()
        time.sleep(2)  # tester can see the red highlighted casino Icon
        # Verify A User Can Access Casino From Matchbook Homepage using top page casino Icon nevigation
    def tearDown(self):
        super(accessablitylivecasinotest, self).tearDown()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    nose.main()