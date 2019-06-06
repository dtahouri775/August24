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
from AdminAuto.Constants import Admin_Dynamic
#from AdminAuto.Locators.AdminMapBonusLinks import AdminBonusLinkMap

class testCreateBonusPlans(BaseTestCase,unittest.TestCase):



    def setUp(self):
        super(testCreateBonusPlans, self).setUp()
        self.navigate_to_page(Admin_Constants['Base_URL'])
        self.driver.maximize_window()

        print("log in was successful")
    def testVerify_a_User_can_Create_allkindof_bonuses_andAssigntoPlayers(self):

        element = HomePageM(self.driver)
        time.sleep(3)
        if(Admin_Dynamic['createallbonuses']=="1"):


            for c in range(1, 7):  # 1:aud  2:cad  3:3ur 4:gbp 5:hkd 6:usd
                for bt in range(1, 8):#Bonus Type=1,2,3,4,5,6,7 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit, Held-Fund)

                    if(c<4 ):
                        continue

                    if(c==4 and bt<3):
                         continue

                    pname=""
                    pname = pname+"AUTO"+Admin_Dynamic['globalname']  # Plan Name:creating for example australian dollar bonus plan
                    tt = bt # Trigger Type=1,2,3,4,5,6,7 (Regular,Match,FreeSpins,NetEntFreeRound,RedtigerFreeRound,Deposit, Held-Fund).
                    pr=0#Priority
                    cur=c#(1: Euro), (2: AUD),(3: HKD),(4: USD),(5: CAD),(6: GBP)
                    curtype=""
                    if (cur == 1):
                        curtype =  curtype + 'aud'
                    if (cur == 2):
                        curtype =  curtype + 'cad'
                    if (cur == 3):
                        curtype =  curtype + 'eur'
                    if (cur == 4):
                        curtype =  curtype + 'gbp'
                    if (cur == 5):
                        curtype =  curtype + 'hkd'
                    if (cur == 6):
                        curtype =  curtype + 'usd'


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
                    #if(c==1 and bt==1):#only one time
                     #   element = HomePageM(self.driver)

                    sdate="06/06/2019"
                    edate="06/01/2029"
                    exdays=1
                    amount=25
                    exd=1
                    rr=0#Rollover Requirement
                    mbl=5#Max Bet Limit
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
                        playername = playername + Admin_Dynamic['globalname'] + curtype + str(bt)  # first player in
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
                    print("Bonus is assigne to player: "+playername)
        if (Admin_Dynamic['createallbonuses'] == "0"):
            print("No bonus creaations is requested")

    def tearDown(self):
            super(testCreateBonusPlans, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()