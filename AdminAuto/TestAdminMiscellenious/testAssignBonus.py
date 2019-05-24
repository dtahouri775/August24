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
from AdminAuto.Locators.AdminMapBonusLinks import AdminBonusLinkMap

class testbonustest(BaseTestCase,unittest.TestCase):



    def setUp(self):
        super(testbonustest, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testVerify_a_User_can_be_assigned_allkindof_Euro_bonuses(self):

        pname=""

        element = HomePageM(self.driver)
        time.sleep(3)
        linkname=""
        for i in range(1, 8):
            pname = "mysqlbeur" +str(i)
            if(i == 1):
                linkname = "linkEuroRegular"
            if (i == 2):
                linkname = "linkEuroMatch"
            if (i == 3):
                linkname = "linkEuroFreeSpins"
            if (i == 4):
                linkname = "linkEuroNetEntFreeRounds"
            if (i == 5):
                linkname = "linkEuroRedTigerBonusSpins"
                     #linkname = "linkEuroDeposit"
            if (i == 6):
                linkname = "linkEuoDeposit"
            if (i == 7):
                linkname = "linkEuoHeldFundsAll"

            element.gotoselectedbonus(linkname)
            text = element.assignbonus(pname,i)
            print(text)

            if(text[:15]=='Users not found'):
                print("Fail")
            if (text[:15] == 'Assigned users:'):
                print("Pass!")

            print("Done!")

    def testVerify_a_User_can_be_assigned_allkindof_Gbp_bonuses(self):

            pname = ""

            element = HomePageM(self.driver)
            time.sleep(3)
            linkname = ""
            for i in range(6, 8):
                pname = "mysqlbgbp" + str(i)
                if (i == 1):
                    linkname = "linkGbpRegular"
                if (i == 2):
                    linkname = "linkGbpMatch"
                if (i == 3):
                    linkname = "linkGbpFreeSpins"
                if (i == 4):
                    linkname = "linkGbpNetEntFreeRounds"
                if (i == 5):
                    linkname = "linkGbpRedTigerBonusSpins"
                    # linkname = "linkEuroDeposit"
                if (i == 6):
                    linkname = "linkGbpDeposit0"
                if (i == 7):
                    linkname = "linkGbpHeldFundsAll"

                element.gotoselectedbonus(linkname)
                text = element.assignbonus(pname, i)
                print(text, i)

                if (text[:15] == 'Users not found'):
                    print("Fail")
                if (text[:15] == 'Assigned users:'):
                    print("Pass!")

                print("Done!")

    def tearDown(self):
            super(testbonustest, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()