'''
Created on December 11, 2018
Change on December 22, 2018
@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
#from CasinoAuto.Pages.LiveCasinoPage import LiveCasinoPageM
from CasinoAuto.Pages.LiveOthersPage import LiveothersPage

class liveotherstest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        print("liveotherstest:Starts")
        super(liveotherstest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()
        print("liveotherstest:Starts")
    def testVerify_A_User_Can_Direct_Launch_Test(self):

            lg_page_obj = LiveothersPage(self.driver)
            lg_page_obj.liveothers()
            ng = lg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            gamecount = lg_page_obj.numberofexistinggamewithname()
            gamecount = lg_page_obj.numberofexistinggamewithname()
            print("Info: Number of games in this(Live Other Games) page equals: ", gamecount)
            lg_page_obj.appendtofile(2, "Info: Number of games in this(Live Other Games) page equals: " + str(gamecount -1 ))
            time.sleep(1)

            for i in range(1, gamecount):
                print('Info  i= ',i)
                exist=lg_page_obj.existgameimage(i)
                if(exist==1):
                    gname=lg_page_obj.click_loginfromlandingpage(i)
                    print("Info gname=",gname)
                    lg_page_obj.logout()
                    time.sleep(1)
                    lg_page_obj.nothanks()
                if (exist == 0):
                    print("Bug GameImage in Live other page Does not exist:  ",i)
                    lg_page_obj.appendtofile(1,"Bug GameImage in Live other page Does not exist:  "+str(i))
                    k=k+1


    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Live Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Live Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
             gname = rg_page_obj.verifylandingpageinfo(i)
             print("Info verify landing page i= ", i)
             rg_page_obj.appendtofile(2, "Info Other Games Page verify landing page i= " + str(i))
    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyproviderlog(i)
            print("Info existing log of i= ", i)
            rg_page_obj.appendtofile(2, "Info Other Games exsisting log of i= " + str(i))
            # verifyproviderlog

    def testverifyexistingofgamename(self):

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygamename(i)
            print("Info game existing of i= ", i)
    def testverifyexistingofdelaername(self):

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifydealername(i)
            if(gname==1):
                print("Info Dealer name existing of i= ", i)
                rg_page_obj.appendtofile(2, "Info Other Games Dealer name existing of i= " + str(i))
            if (gname == 0):
                print("Bug Dealer name in live others page is not existing of i= ", i)
                rg_page_obj.appendtofile(1, "Bug GameImage in Live other page Does not exist:  " + str(i))
    def testverifyexistingofminmax(self):

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygameminmax(i)
            if(gname==1):
                print("Info Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(2, "Info Other Games Existing min-max of  i= " + str(i))
            if (gname == 0):
                print("Bug: NOt Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(1, "Bug GameImage in Live other page Does not exist:  " + str(i))


    def testVerifyCurrentNumberOfPlayersUpdateForOtherGames (self):#may improve this game in future by playing game

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        oldhistory = []
        for i in range(1, gamecount):
            seat = rg_page_obj.verifyupdateseats(i)
            oldhistory.append(seat)
        rg_page_obj.navaigatetofeaturepage()
        print("oldhistory =", oldhistory)

        time.sleep(60)
        rg_page_obj.liveothers()
        newhistory = []
        for i in range(1, gamecount):  # footer images are deducted (- 5)
            seat = rg_page_obj.verifyupdateseats(i)
            newhistory.append(seat)
        compar_result = cmp(newhistory, oldhistory)
        print(" compar_result =", compar_result)

        if (compar_result == 0):
            print("Bug : None of the game seats result are updated in the last one minute!")
            rg_page_obj.appendtofile(1, "Bug :@VerifyCurrentNumberOfPlayersUpdateForOtherGames None of the game seats result are updated in one minute, may be none played the game! ")
            print("newhistory = ", newhistory)
            rg_page_obj.appendtofile(1, "newhistory =" + str(newhistory))
            print("oldhistory = ", oldhistory)
            rg_page_obj.appendtofile(1, "oldhistory =" + str(oldhistory))
            if (compar_result != 0):
                print("newhistory = ", newhistory)
                print("oldhistory = ", oldhistory)


    def testVerifyDreamCatcherResultsUpdateDuringNavigationOfTheLobby (self):#smart putll test

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        oldhistory = []
        for i in range(1, gamecount):
            gname = rg_page_obj.returngamename(i)
            if (gname == 'Dream Catcher'):
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                oldhistory.append(historymainpage)
            else:
                continue


        rg_page_obj.navaigatetofeaturepage()
        print("oldhistory =", oldhistory)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)  # wait for 60 second to make sure the results will be updated

        rg_page_obj.liveothers()#return to Others page again
        newhistorymainpage = []
        newhistory = []
        for i in range(1,gamecount):  # -7 just in case some of the games has been removed
            gname = rg_page_obj.returngamename(i)
            if (gname == 'Dream Catcher' and i!=3):
                newhistorymainpage = rg_page_obj.verifyavailablenumbers(i)
                newhistory.append(newhistorymainpage)
            else:
                continue
            #print("newhistorymainpage=", newhistorymainpage)
        print("newhistory =",newhistory )
        compar_result=cmp(newhistory,oldhistory)
        print(" compar_result =",  compar_result)
        if(compar_result==0):
            if (compar_result == 0):
                print("Bug Failure: None of the game history result are updated For Evolution games!")
                rg_page_obj.appendtofile(1,"Bug Failure: Deream Catcher game history result are not updated !")
                print("newhistory = ", newhistory)
                rg_page_obj.appendtofile(1, "newhistory =" + str(newhistory))
                print("oldhistory = ", oldhistory)
                rg_page_obj.appendtofile(1, "oldhistory =" + str(oldhistory))

        if(compar_result != 0):
            print("info: Pass the test: VerifyDreamCatcherResultsUpdateDuringNavigationOfTheLobby")
            rg_page_obj.appendtofile(2, "Info VerifyDreamCatcherResultsUpdateDuringNavigationOfTheLobby")
            rg_page_obj.appendtofile(2,"info: Pass the test: VerifyDreamCatcherResultsUpdateDuringNavigationOfTheLobby")

    def testVerifyOthersGameResultsUpdateonLandingPageDuringNavigation(self):#smart putll test

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        historymainpage = []
        historylandingpage = []
        oldhistory = []
        bug_mismatch = 0
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.returngamename(i)
            if(gname == 'Dream Catcher' and i != 3):#We need to add game names here based on games added here or modify our current datahook naming
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                historylandingpage = rg_page_obj.verifyavailablenumberslandingpage(i)
            if(historymainpage==historylandingpage):
                print(" ")
                print("Info: numbers in main page and landing pager are matching game_num=", i)
                #print("Info: numbers in main page and landing pager are matching game_num=",i)
            if (historymainpage != historylandingpage ):
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                if (historymainpage == historylandingpage):
                    print("Info: numbers in main page and landing pager are matching after second trygame_num=", i)
                    rg_page_obj.appendtofile(2,
                                             "Info: numbers in main page and landing pager are matching after second trygame_num=" + str(
                                                 i))
                    continue

                print("Bug: Other Games Page numbers in main page and landing pager are not matching game_num=", i)
                rg_page_obj.appendtofile(1, "Bug: Others Page Games @testVerifyOthersGameResultsUpdateonLandingPageDuringNavigation numbers in main page and landing pager are not matching game_num="+ str(i))
                print("historymainpage=", historymainpage)
                rg_page_obj.appendtofile(1,"historymainpage=" + str(historymainpage))
                print("historylandingpage=", historylandingpage)
                rg_page_obj.appendtofile(1, "historylandingpage=" + str(historylandingpage))
                bug_mismatch=bug_mismatch+1#for any mismatch
    def testVerifyCurrentNumberOfPlayersUpdateForOtherGamesOnlandingpage (self):#smart putll test

        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        time.sleep(1)
        historymainpage = []
        historylandingpage =[]
        bug_mismatch =0
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Other Games) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Other Games) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.returngamename(i)
            if(gname == 'Dream Catcher' and i != 3):#We need to add game names here based on games added here or modify our current datahook naming
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                historylandingpage = rg_page_obj.verifyavailablenumberslandingpage(i)
            if (gname != 'Dream Catcher'):
                historymainpage = rg_page_obj.verifyupdateseats(i)
                historylandingpage = rg_page_obj.verifyupdateseatslandingpage(i)
                print(" ")

            if(historymainpage==historylandingpage):
                print(" ")
                print("Info: numbers in main page and landing pager are matching game_num=", i)
                #print("Info: numbers in main page and landing pager are matching game_num=",i)
            if (historymainpage != historylandingpage ):
                print("Bug: Other Games Page numbers in main page and landing pager are not matching game_num=", i)
                rg_page_obj.appendtofile(1, "Bug: Others Page @testVerifyCurrentNumberOfPlayersUpdateForOtherGamesOnlandingpage Games numbers in main page and landing pager are not matching game_num="+ str(i))
                print("historymainpage=", historymainpage)
                rg_page_obj.appendtofile(1,"historymainpage=" + str(historymainpage))
                print("historylandingpage=", historylandingpage)
                rg_page_obj.appendtofile(1, "historylandingpage=" + str(historylandingpage))
                bug_mismatch=bug_mismatch+1#for any mismatch

    def testVerify_A_User_Can_Sort_OtherGames_Name_Descending_By_Clicking_text_ZAtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,1)#1 means using text for sorting

    def testVerify_A_User_Can_Sort_OtherGames_Name_Ascending_By_Clicking_text_AZtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_OtherGames_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,2)#2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_OtherGames_Name_By_Displayed_Ascending_Arrowtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,2)#2 means using arrow for sorting

    def testVerify_A_User_Can_Sort_OtherGames_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount, 2)  # 2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_OtherGames_Stake_Size_Descending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_OtherGames_Stake_Size_Ascending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,1)#1 means using text for sorting


     #Sorting by arrow directions


    def testVerify_A_User_Can_Sort_OtherGames_Stake_Size_Descending_By_Clicking_Arrow_Uptest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_A_User_Can_Sort_OtherGames_Stake_Size_Ascending_By_Clicking_Arrow_Downtest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_Refreshing_OtherGames_Page_Display_Default_Assending_Sort_by_Game_Namestest(self):
        rg_page_obj = LiveothersPage(self.driver)
        rg_page_obj.liveothers()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(OtherGames) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(OtherGames) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount, 1)  # 1 means using text for sorting

        #gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount, 2)  # 2 means using arrow for sorting
    def testVerify_Sort_Arrow_is_existing_in_OtherGames_Pagetest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(6)  # existing of sort arrow
    def testVerify_text_Sortby_is_existing_in_OtherGames_Pagetest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(5)  #
        print(name)
        if (name == 'Sort by:'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Other Games Stake Size text is existing:")

    def testVerify_text_StakeSize_is_existing_in_OtherGames_Pagetest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(4)  #
        print(name)
        if (name == 'Stake Size'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Other Games Stake Size text is existing:")

    def testVerify_text_ZA_changes_to_AZ_by_clicking_in_OtherGames_Pagetest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(3)  #
        print(name)
        if (name == 'A-Z'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Other Games Z-A changes to A-Z for sorting:")

    def testVerify_text_AZ_changes_to_ZA_by_clicking_in_Page_OtherGamestest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(2)  #
        print(name)
        if (name == 'Z-A'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Other Games A-Z changes to Z-A for sorting:")

    def testVerify_text_AZ_is_existing_in_OtherGames_Pagetest(self):
        bj_page_obj = LiveothersPage(self.driver)
        bj_page_obj.liveothers()
        name = bj_page_obj.pageverificationelementexisting(1)#1 means verify exising of A-z
        print(name)
        if(name=='A-Z'):
            print("Pass!")
            bj_page_obj.appendtofile(2,"Other Games A-Z existing for sorting:")

    def tearDown(self):
        print("liveotherstest:ended")
        super(liveotherstest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()