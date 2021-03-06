'''
Created on May 23, 2019

@author: Daryoush
git added

'''

import unittest
import nose
import time

from CasinoAuto.Pages.BaseTestCase import BaseTestCase
#from CasinoAuto.Pages.HomePageM import HomePageM
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Constants import Admin_Dynamic
from AdminAuto.Pages.RegisterUsersPages import RegisterUserPages

class uiconsitentadmin(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(uiconsitentadmin, self).setUp()
        self.navigate_to_page(Admin_Constants['Client_URL'])
        self.driver.maximize_window()
        print("Access to dev06 client was successful")

    def testavisiblitybonusymobl(self):
       page_obj = RegisterUserPages(self.driver)
       for c in range(1, 7):  # 1:eur  2:aud  3:hkd 4:usd 5:cad 6:gbp
           for bt in range(1, 7):  # Bonus Type=1,2,3,4,5,6 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit)
               #if(bt==1):#/debyg purpose only should by by passed once it is done!!
                #   continue

               cur = c  # (1: Euro), (2: AUD),(3: HKD),(4: USD),(5: CAD),(6: GBP)
               curtype = ""
               if (cur == 1):
                   curtype = curtype + 'eur'
               if (cur == 2):
                   curtype = curtype + 'aud'
               if (cur == 3):
                   curtype = curtype + 'hkd'
               if (cur == 4):
                   curtype = curtype + 'usd'
               if (cur == 5):
                   curtype = curtype + 'cad'
               if (cur == 6):
                   curtype = curtype + 'gbp'
               #username="May21"+curtype+str(bt)
               username = Admin_Dynamic['globalname'] + curtype + str(bt)
               password=Admin_Dynamic['uipassword']
               page_obj.login(username,password)
               page_obj.verifybonsuicon(username)
               time.sleep(2)
               page_obj.logout()
               time.sleep(1)

    def testbactivateassignedbonus(self):
       page_obj = RegisterUserPages(self.driver)
       for c in range(1, 7):  # 1:eur  2:aud  3:hkd 4:usd 5:cad 6:gbp
           for bt in range(1, 7):  # Bonus Type=1,2,3,4,5,6 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit)
               #if (bt < 2):  # /debyg purpose only should by by passed once it is done!!
                #   continue
               cur = c  # (1: Euro), (2: AUD),(3: HKD),(4: USD),(5: CAD),(6: GBP)
               curtype = ""
               if (cur == 1):
                   curtype = curtype + 'eur'
               if (cur == 2):
                   curtype = curtype + 'aud'
               if (cur == 3):
                   curtype = curtype + 'hkd'
               if (cur == 4):
                   curtype = curtype + 'usd'
               if (cur == 5):
                   curtype = curtype + 'cad'
               if (cur == 6):
                   curtype = curtype + 'gbp'

               username=Admin_Dynamic['globalname']+curtype+str(bt)
               password=Admin_Dynamic['uipassword']
               page_obj.login(username,password)
               trigertype=""
               if (bt == 1):
                   trigertype = trigertype + 'Regular'
               if (bt == 2):
                   trigertype = trigertype + 'Match'
               if (bt == 3):
                   trigertype = trigertype + 'MBFS'
               if (bt == 4):
                   trigertype = trigertype + 'NTFS'
               if (bt == 5):
                   trigertype = trigertype + 'RTFS'
               if (bt == 6):
                   trigertype = trigertype + 'Deposit'
               if (bt == 7):
                   trigertype = trigertype + 'HF'
               bonusname="Auto"+Admin_Dynamic['globalname']+curtype+trigertype+str(1)
               page_obj.verifybonsuicon(username)
               time.sleep(2)
               page_obj.verifexistingbounstitle(bonusname)
               page_obj.claimassignedBonus()

               time.sleep(2)
               page_obj.logout()
               time.sleep(10)


    def tearDown(self):
        super(uiconsitentadmin, self).tearDown()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    nose.main()