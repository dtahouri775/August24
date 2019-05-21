'''
Created on Feb07 , 2019

@author: Daryoush
'''

import unittest
import nose
import time
from AdminAuto.Pages.BaseTestCase import BaseTestCase
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Pages.HomePageM import HomePageM
from CasinoAuto.Pages.LiveOthersPage import LiveothersPage

class testdreamcatchertest(BaseTestCase,unittest.TestCase):



    def setUp(self):
        super(testdreamcatchertest, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testVerifyDreamCatcherResultsUpdateDuringNavigationOfTheLobby(self):
        adminthistory = []
        element = HomePageM(self.driver)
        element.clickAdminstration()
        # I may need to find criteria for how many games are presented in admin Evo live game page, if might be more than 1000
        for i in range(1,1000):
            adminthistory = element.recordDreamCatcherResultsfromadmin(i)
            print("adminthistory = ", adminthistory)
            gname =  adminthistory[2]#third tab is game name
            ghistory =  adminthistory[6]#7th tab is game history
            if (gname == 'Dream Catcher'):
                break

        print("gname=",gname)
        print("adminthistory[6]=",adminthistory[6])
        time.sleep(100)
        self.driver.get("https://dev06.xcl.ie/casino/live/other")#may added for constants
        gamethistory1 = []#game history in front page
        rg_page_obj = LiveothersPage(self.driver)
        ng = rg_page_obj.getgamenumber()
       # print("Info Number of images in this page equals: ", ng)
        time.sleep(1)
        for i in range(1, ng - 10):  # footer images are deducted (- 5)
            gname = rg_page_obj.returngamename(i)
            print("gname= ", gname)
            if (gname == 'Dream Catcher'):
                print("Found Dream Catcher")
                break
        print("Info game existing of i= ", i)
        gamethistory1 = rg_page_obj.returngamehistorypage(i)
        print("gamethistory1=",gamethistory1)
        print(i)

    def tearDown(self):
            super(testdreamcatchertest, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()