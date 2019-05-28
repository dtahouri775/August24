'''
Created on May09 , 2019

@author: Daryoush
'''

import unittest
import nose
import time
from AdminAuto.Pages.BaseTestCase import BaseTestCase
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Pages.HomePageM import HomePageM
#from AdminAuto.Locators.AdminMapBonusLinks import AdminBonusLinkMap

class testfundplayer(BaseTestCase,unittest.TestCase):



    def setUp(self):
        super(testfundplayer, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testVerify_a_User_can_be_fund_Euro_1M(self):#work from here on Monday

        pname=""

        element = HomePageM(self.driver)
        time.sleep(3)
        linkname=""
        pname = "mysqleur1"#will fund this user 1M

        linkname = "linkEur1M"

        element.gotoselectedbonus(linkname)
        text = element.assignbonus(pname,1000)#clue for direct access to assign
        #claim bonous and load a game

        print(text)

        if(text[:15]=='Users not found'):
            print("Fail")
        if (text[:15] == 'Assigned users:'):
            print("Pass!")

            print("Done!")


    def tearDown(self):
            super(testfundplayer, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()