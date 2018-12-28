'''
Created on December 11, 2018
Change on December 20, 2018
Change on December 28, 2018
@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
#from CasinoAuto.Pages.LiveCasinoPage import LiveCasinoPageM
from CasinoAuto.Pages.LiveBlackjackPage import LiveblackjackPage

class liveblackjacktest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(liveblackjacktest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def testVerify_A_User_Can_Direct_Launch_Blackjack_Test(self):

            lg_page_obj = LiveblackjackPage(self.driver)
            lg_page_obj.liveblackjack()
            ng = lg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            print("Info: Number of images in this page equals: ",ng)
            time.sleep(5)
            k=0
            for i in range(1, ng - 10):  # footer images are deducted (- 5), and there are additional image on this page too
                print('Info: i= ',i)
                exist=lg_page_obj.existgameimage(i)
                try:  # just to make sure that the issue is not Nothanks button that randomly appears in Blackjack page
                    lg_page_obj.nothanks(self.driver)
                    print("No thanks button is clicked")
                    time.sleep(1)
                except:
                    print("Info No thanks button is not there to click which is ok ")

                if (exist == 1):
                    gname = lg_page_obj.click_loginfromlandingpage(i)
                    print("Info gname=",gname)
                    lg_page_obj.logout()
                    time.sleep(3)
                    print("Info Successful Log out")

                if (exist == 0):
                    print("Bug  Black jack Page Log in  Directly issue:  Ement=", i)
                    time.sleep(3)
                time.sleep(3)
                try:  # just to make sure that the issue is not Nothanks button that randomly appears
                    lg_page_obj.nothanks(self.driver)
                    print("No thanks button is clicked")
                    time.sleep(1)
                except:
                    print("Info No thanks button is not there to click which is ok ")

    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info: Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng-10):  # footer images are deducted (- 5), and there are additional image on this page too
             gname = rg_page_obj.verifylandingpageinfo(i)
             print("Info: Testing to Verify landing page i= ", i)
    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng-10):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifyproviderlog(i)
            print("Info: Tested existing log of i= ", i)
            # verifyproviderlog

    def testverifyexistingofgamename(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 6):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifygamename(i)
            print("Info: Tested game existing of i= ", i)
    def testverifyexistingofdelaername(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info: Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 6):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifydealername(i)
            print("Info: Tested Dealer name existing of i= ", i)
    def testverifyexistingofminmax(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info:Number of game in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 10):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifygameminmax(i)
    def testVerifyGameTileDisplaysAvailableSeatsForBlackjack(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info:Number of game in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 10):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifyavailableseats(i)
    def tearDown(self):
        super(liveblackjacktest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()