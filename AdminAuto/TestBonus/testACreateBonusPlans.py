'''
Created on May14 , 2019

@author: Daryoush
'''

import unittest
import nose
import time
from AdminAuto.Pages.BaseTestCase import BaseTestCase
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Pages.HomePageM import HomePageM
from AdminAuto.Locators.AdminMapBonusLinks import AdminBonusLinkMap

class testCreateBonusPlans(BaseTestCase,unittest.TestCase):



    def setUp(self):
        super(testCreateBonusPlans, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testVerify_a_User_can_Create_allkindof_bonuses_andAssigntoPlayers(self):


        for c in range(1, 7):  # 1:eur  2:aud  3:hkd 4:usd 5:cad 6:gbp
            for bt in range(1, 8):#Bonus Type=1,2,3,4,5,6,7 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit, Held-Fund)
                pname=""
                pname = pname+"AUTOMay21"  # Plan Name:creating for example australian dollar bonus plan
                tt = bt # Trigger Type=1,2,3,4,5,6,7 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit, Held-Fund).
                pr=0#Priority
                cur=c#(1: Euro), (2: AUD),(3: HKD),(4: USD),(5: CAD),(6: GBP)
                curtype=""
                if (cur == 1):
                    curtype =  curtype + 'eur'
                if (cur == 2):
                    curtype =  curtype + 'aud'
                if (cur == 3):
                    curtype =  curtype + 'hkd'
                if (cur == 4):
                    curtype =  curtype + 'usd'
                if (cur == 5):
                    curtype =  curtype + 'cad'
                if (cur == 6):
                    curtype =  curtype + 'gbp'


                trigertype=""
                if (bt == 1):
                    trigertype =  trigertype + 'Regular'
                if (bt == 2):
                    trigertype =  trigertype + 'Match'
                if (bt == 3):
                    trigertype =  trigertype + 'MBFS'
                if (bt == 4):
                    trigertype =  trigertype + 'NTFS'
                if (bt == 5):
                    trigertype =  trigertype + 'RTFS'
                if (bt == 6):
                    trigertype =  trigertype + 'Deposit'
                if (bt == 7):
                    trigertype = trigertype + 'HF'


                pname = pname + curtype+ trigertype+str(1)

                st=1#Status=1, means active 2 non active
                if(c==1 and bt==1):#only one time
                    element = HomePageM(self.driver)

                sdate="05/21/2019"
                edate="05/01/2029"
                exdays=1
                amount=10
                exd=1
                rr=1#Rollover Requirement
                mbl=2#Max Bet Limit
                ucr=1#Use Contribution Rate checked, 0 means unchecked
                fdg=1#for Desktop games checked, 0 means unchecked
                fmg=1#for Mobile gameschecked, 0 means unchecked
                ips=15#Included Platforms Status Check All 15(1111), uucheck all zero(0000)
                igs=1#Included Games 1: Check All, 2: Unchcek All 3: Expan

                url="linkcreatebonus"
                element.gotoselectedbonus(url)
                result=element.createbonusplan(pname,pr,cur,tt,st,sdate,edate,exd,amount,rr,mbl,ucr,fdg,fmg,ips,igs)
                if(result=="Success"):
                    print("Bonus created")
                else:
                    print("Fail: Bonus is not created!")

                plassign = 1  # if zero means only creat bonus plan 1 means assing to player too
                playername = ""
                # Enter players info here!!
                if (plassign == 1):
                    playername = playername + "May21" + curtype + str(bt)  # first player in
                time.sleep(3)
                if(bt==7):#No need to assign held fund bonus
                    continue
                text=element.assignbonus(playername,tt)
                print(text)
                if (text[:15] == 'Users not found'):
                    print("Fail")
                if (text[:15] == 'Assigned users:'):
                    print("Pass!")

                print("Done!")

    def tearDown(self):
            super(testCreateBonusPlans, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()