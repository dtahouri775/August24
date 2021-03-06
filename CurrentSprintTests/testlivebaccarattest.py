'''
Created on December 11, 2018
Change on December 20, 2018
@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.LiveBaccaratPage import LivebaccaratPage
import datetime
class livebaccarattest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        print("livebaccarattest:Starts")

        super(livebaccarattest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()
        print(datetime.datetime.now())
        lg_page_obj = LivebaccaratPage(self.driver)
        lg_page_obj.appendtofile(2, "Baccarat Game Started: ")
        lg_page_obj.appendtofile(2, str(datetime.datetime.now()))
       #lg_page_obj.appendtofile(1, "Baccarat Game Started: ")
        #lg_page_obj.appendtofile(1, str(datetime.datetime.now()))


    def testVerify_A_User_Can_Sort_Baccarat_Name_Descending_By_Clicking_text_ZAtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,1)#1 means using text for sorting

    def testVerify_A_User_Can_Sort_Baccarat_Name_Ascending_By_Clicking_text_AZtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Baccarat_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,2)#2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Baccarat_Name_By_Displayed_Ascending_Arrowtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,2)#2 means using arrow for sorting

    def testVerify_A_User_Can_Sort_Baccarat_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount, 2)  # 2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Baccarat_Stake_Size_Descending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Baccarat_Stake_Size_Ascending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,1)#1 means using text for sorting


     #Sorting by arrow directions


    def testVerify_A_User_Can_Sort_Baccarat_Stake_Size_Descending_By_Clicking_Arrow_Uptest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_A_User_Can_Sort_Baccarat_Stake_Size_Ascending_By_Clicking_Arrow_Downtest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_Refreshing_Baccarat_Page_Display_Default_Assending_Sort_by_Game_Namestest(self):
        rg_page_obj = LivebaccaratPage(self.driver)
        rg_page_obj.livebaccarat()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Baccarat) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Baccarat) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount, 1)  # 1 means using text for sorting

        #gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount, 2)  # 2 means using arrow for sorting
    def testVerify_Sort_Arrow_is_existing_in_Baccarat_Pagetest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(6)  # existing of sort arrow
    def testVerify_text_Sortby_is_existing_in_Baccarat_Pagetest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(5)  #
        print(name)
        if (name == 'Sort by:'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Baccarat Game Stake Size text is existing:")

    def testVerify_text_StakeSize_is_existing_in_Baccarat_Pagetest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(4)  #
        print(name)
        if (name == 'Stake Size'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Baccarat Game Stake Size text is existing:")

    def testVerify_text_ZA_changes_to_AZ_by_clicking_in_Baccarat_Pagetest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(3)  #
        print(name)
        if (name == 'A-Z'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Baccarat Game Z-A changes to A-Z for sorting:")

    def testVerify_text_AZ_changes_to_ZA_by_clicking_in_Page_Baccarattest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(2)  #
        print(name)
        if (name == 'Z-A'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Baccarat Game A-Z changes to Z-A for sorting:")

    def testVerify_text_AZ_is_existing_in_Baccarat_Pagetest(self):
        bj_page_obj = LivebaccaratPage(self.driver)
        bj_page_obj.livebaccarat()
        name = bj_page_obj.pageverificationelementexisting(1)#1 means verify exising of A-z
        print(name)
        if(name=='A-Z'):
            print("Pass!")
            bj_page_obj.appendtofile(2,"Baccarat Game A-Z existing for sorting:")

    def tearDown(self):
        print("livebaccarattest:Ended")
        lg_page_obj = LivebaccaratPage(self.driver)
        lg_page_obj.appendtofile(2, "Baccarat Game Finished Testing: ")
        lg_page_obj.appendtofile(2, str(datetime.datetime.now()))
        #lg_page_obj.appendtofile(1, "Finished Testing:  ")
        #lg_page_obj.appendtofile(1, str(datetime.datetime.now()))
        super(livebaccarattest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()