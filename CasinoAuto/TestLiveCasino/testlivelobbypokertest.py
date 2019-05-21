'''
Created on December 11, 2018
Change on December 20, 2018
@author: Daryoush
Change on January 24, 2019
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.LivePokerPage import LivepokerPage
import datetime
class livepokertest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(livepokertest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()
        print("livepokertest:Starts")
        sg_page_obj = LivepokerPage(self.driver)
        sg_page_obj.appendtofile(2, "Poker Game Started: ")
        sg_page_obj.appendtofile(2, str(datetime.datetime.now()))

    def testVerify_A_User_Can_Direct_Launch_Test(self):

            lg_page_obj = LivepokerPage(self.driver)
            lg_page_obj.livepoker()
            ng = lg_page_obj.getgamenumber()
            deductedimage = lg_page_obj.getdeductedimage()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10
            gamecount = lg_page_obj.numberofexistinggamewithname()
            print("Info: Number of games in this(Poker) page equals: ", gamecount)
            lg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
            time.sleep(1)

            for i in range(1, gamecount):
                print('Info: i= ',i)
                exist=lg_page_obj.existgameimage(i)
                if(exist==1):
                    gname=lg_page_obj.click_loginfromlandingpage(i)
                    #print("Info: gname=",gname)
                    lg_page_obj.logout()
                    time.sleep(1)
                    lg_page_obj.nothanks()
                if (exist == 0):
                    lg_page_obj.appendtofile(1, "Bug:GameImage In Poker Page Does not exist:  gname=: " + str(i))
                    print("Bug:GameImage In Poker Page Does not exist:  gname=",i)
                    k=k+1
    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
             gname = rg_page_obj.verifylandingpageinfo(i)
             print("Info: verify landing page in Poker games for the required information i= ", i)
             rg_page_obj.appendtofile(2, "Info: Number of games in this page equals ng =" + str(i))

    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyproviderlog(i)
            print("Info: existing In poker page log of i= ", i)
            rg_page_obj.appendtofile(2, "Info: Info: existing in Poker page log of  i=" + str(i))
            # verifyproviderlog

    def testverifyexistingofgamename(self):

        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygamename(i)
            print("Info: Game existing of i= ", i)
            rg_page_obj.appendtofile(2, "Info: Game existing of i=" + str(i))
    def testverifyexistingofdelaername(self):

        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifydealername(i)
            if(gname==1):
                print("Info: Dealer name In Poker Page existing of i= ", i)
                rg_page_obj.appendtofile(2, "Info: Dealer name In Poker Page existing of i=" + str(i))
            if (gname == 0):
                print("Bug: Dealer name in Poker page is not existing of i= ", i)
                rg_page_obj.appendtofile(1, "Bug: Dealer name in Poker page is not existing of game=" + str(i))

    def testverifyexistingofminmax(self):

        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygameminmax(i)
            if(gname==1):
                print("Info Poker Page : Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(2, "Info: Min-Max existing of i=" + str(i))
            if (gname == 0):
                print("Bug: Poker Page NOt Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(1, "Info: Poker Page Not existing of min-max i=" + str(i))
    def testVerifyGameTileDisplaysAvailableSeatsForPoker(self):

        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyavailableseats(i)
            if (gname == 1):
                print("Info Existing of Display Seat available  i= ", i)
                rg_page_obj.appendtofile(2, "Info: Min-Max existing of i=" + str(i))
            if (gname == 0):
                print("Bug: NOt Existing of Seat available  game= ", i)
                rg_page_obj.appendtofile(1, "Bug:@VerifyGameTileDisplaysAvailableSeatsForPoker NOt Existing of Seat available  game= " + str(i))

    #Verify Current Number Of Players Update On Poker During Navigation of The Lobby
    def testVerifyCurrentNumberOfPlayersUpdateOnPokerDuringNavigationofTheLobby(self):#may improve this game in future by playing game

        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            deductedimage = 3

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        oldhistory = []
        for i in range(1, gamecount):
            seat = rg_page_obj.verifyupdateseats(i)
            oldhistory.append(seat)
        rg_page_obj.navaigatetofeaturepage()
        print("oldhistory =", oldhistory)

        time.sleep(60)
        rg_page_obj.livepoker()
        newhistory = []
        for i in range(1, deductedimage+1):  # footer images are deducted (- 5)
            seat = rg_page_obj.verifyupdateseats(i)
            newhistory.append(seat)
        compar_result = cmp(newhistory, oldhistory)
        print(" compar_result =", compar_result)

        if (compar_result == 0):
            print("Bug : None of the game seats result are updated in the last one minute!")
            rg_page_obj.appendtofile(1, "Bug :@VerifyCurrentNumberOfPlayersUpdateOnPokerDuringNavigationofTheLobby None of the game seats result are updated in one minute, may be none played the game! ")
            print("newhistory = ", newhistory)
            rg_page_obj.appendtofile(1, "newhistory =" + str(newhistory))
            print("oldhistory = ", oldhistory)
            rg_page_obj.appendtofile(1, "oldhistory =" + str(oldhistory))
            if (compar_result != 0):
                print("newhistory = ", newhistory)
                print("oldhistory = ", oldhistory)

    #Verify Current Number Of Players for Poker Update on Landing Page During Navigation


    def testVerifyCurrentNumberOfPlayersforPokerUpdateonLandingPageDuringNavigation(self):#smart putll test
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            deductedimage = 3
        newlandingpagenum =[]
        historylandingpage=[]

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            landingpagenum = rg_page_obj.verifyupdateseatslandingpage(i)
            historylandingpage.append(landingpagenum)
            print("landingpagenum=", landingpagenum)



        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)
        rg_page_obj.livepoker()
        for i in range(1, deductedimage + 1):
            landingpagenum = rg_page_obj.verifyupdateseatslandingpage(i)
            newlandingpagenum.append(landingpagenum)
            print("newlandingpage=", landingpagenum)

        if(historylandingpage!=newlandingpagenum):
                print(" ")
                print("Info: Player number in landing pager are matching afgame_num=", i)
                #print("Info: numbers in main page and landing pager are matching game_num=",i)
        if(historylandingpage==newlandingpagenum):
                print("Bug: Poker Page numbers in landing pager are not updated game_num=", i)
                rg_page_obj.appendtofile(1, "Bug: Poker Page @VerifyCurrentNumberOfPlayersforPokerUpdateonLandingPageDuringNavigation Number of Players in landing pager are not updated="+ str(i))
        print("historymainpage=", historylandingpage)
        rg_page_obj.appendtofile(1,"Bug: Poker Page historymainpage=" + str(historylandingpage))
        print("historylandingpage=", historylandingpage)
        rg_page_obj.appendtofile(1, "Bug: Poker Page historylandingpage=" + str(historylandingpage))

    def testVerify_A_User_Can_Sort_Poker_Name_Descending_By_Clicking_text_ZAtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,1)#1 means using text for sorting

    def testVerify_A_User_Can_Sort_Poker_Name_Ascending_By_Clicking_text_AZtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Poker_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,2)#2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Poker_Name_By_Displayed_Ascending_Arrowtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,2)#2 means using arrow for sorting

    def testVerify_A_User_Can_Sort_Poker_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount, 2)  # 2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Poker_Stake_Size_Descending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Poker_Stake_Size_Ascending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,1)#1 means using text for sorting


     #Sorting by arrow directions


    def testVerify_A_User_Can_Sort_Poker_Stake_Size_Descending_By_Clicking_Arrow_Uptest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_A_User_Can_Sort_Poker_Stake_Size_Ascending_By_Clicking_Arrow_Downtest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_Refreshing_Poker_Page_Display_Default_Assending_Sort_by_Game_Namestest(self):
        rg_page_obj = LivepokerPage(self.driver)
        rg_page_obj.livepoker()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Poker) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Poker) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount, 1)  # 1 means using text for sorting

        #gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount, 2)  # 2 means using arrow for sorting
    def testVerify_Sort_Arrow_is_existing_in_Poker_Pagetest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(6)  # existing of sort arrow
    def testVerify_text_Sortby_is_existing_in_Poker_Pagetest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(5)  #
        print(name)
        if (name == 'Sort by:'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Poker Game Stake Size text is existing:")

    def testVerify_text_StakeSize_is_existing_in_Poker_Pagetest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(4)  #
        print(name)
        if (name == 'Stake Size'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Poker Game Stake Size text is existing:")

    def testVerify_text_ZA_changes_to_AZ_by_clicking_in_Poker_Pagetest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(3)  #
        print(name)
        if (name == 'A-Z'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Poker Game Z-A changes to A-Z for sorting:")

    def testVerify_text_AZ_changes_to_ZA_by_clicking_in_Page_Pokertest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(2)  #
        print(name)
        if (name == 'Z-A'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Poker Game A-Z changes to Z-A for sorting:")

    def testVerify_text_AZ_is_existing_in_Poker_Pagetest(self):
        bj_page_obj = LivepokerPage(self.driver)
        bj_page_obj.livepoker()
        name = bj_page_obj.pageverificationelementexisting(1)#1 means verify exising of A-z
        print(name)
        if(name=='A-Z'):
            print("Pass!")
            bj_page_obj.appendtofile(2,"Poker Game A-Z existing for sorting:")
    def tearDown(self):
        print("livepokertest:Ended")
        super(livepokertest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()