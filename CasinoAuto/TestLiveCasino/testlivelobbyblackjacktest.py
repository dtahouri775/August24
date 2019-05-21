'''
Created on December 11, 2018
Change on December 20, 2018
Change on December 28, 2018
Change on January 24, 2019
@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
#from CasinoAuto.Pages.LiveCasinoPage import LiveCasinoPageM
from CasinoAuto.Pages.LiveBlackjackPage import LiveblackjackPage
import datetime
class liveblackjacktest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        print("liveblackjacktest:Starts")
        super(liveblackjacktest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()
        print(datetime.datetime.now())
        sg_page_obj = LiveblackjackPage(self.driver)
        sg_page_obj.appendtofile(2, "BlackJack Game Started: ")
        sg_page_obj.appendtofile(2, str(datetime.datetime.now()))
        #sg_page_obj.appendtofile(1, "BlackJack Game Game Started: ")
        #sg_page_obj.appendtofile(1, str(datetime.datetime.now()))


    def testVerify_A_User_Can_Direct_Launch_Blackjack_Test(self):

            lg_page_obj = LiveblackjackPage(self.driver)
            lg_page_obj.liveblackjack()
            ng = lg_page_obj.getgamenumber()
            deductedimage = lg_page_obj.getdeductedimage()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            #print("Info: Number of images in this page equals: ",ng)
            print("Info: Number of games in this page equals: ", deductedimage)
            lg_page_obj.appendtofile(2,"Info: Number of games in this page equals: "+str(deductedimage))
            time.sleep(1)
            k=0
            for i in range(1,deductedimage+1):  # footer images are deducted (- 5), and there are additional image on this page too
                #print('Info: i= ',i)
                exist=lg_page_obj.existgameimage(i)
                try:  # just to make sure that the issue is not Nothanks button that randomly appears in Blackjack page
                    lg_page_obj.nothanks(self.driver)
                    print("No thanks button is clicked")
                    time.sleep(1)
                except:
                    print(" ")
                    #print("Info No thanks button is not there to click which is ok ")

                if (exist == 1):
                    gname = lg_page_obj.click_loginfromlandingpage(i)
                    #print("Info gname=",gname)
                    lg_page_obj.logout()
                    time.sleep(1)
                    #print("Info Successful Log out")

                if (exist == 0):
                    print("")
                    time.sleep(1)
                time.sleep(1)
                try:  # just to make sure that the issue is not Nothanks button that randomly appears
                    lg_page_obj.nothanks(self.driver)
                    print(" ")
                    #print("No thanks button is clicked")
                    time.sleep(1)
                except:
                    print(" ")
                    #print("Info No thanks button is not there to click which is ok ")

    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        deductedimage=rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount=rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2,"Info: Number of games in this(BlackJack) page equals: "+ str(gamecount))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifylandingpageinfo(i)
             #print("Info: Testing to Verify landing page i= ", i)
    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyproviderlog(i)
            #print("Info: Tested existing log of i= ", i)
            # verifyproviderlog

    def testverifyexistingofgamename(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygamename(i)
            print(gname)
            #print("Info: Tested game existing of i= ", i)
    def testverifyexistingofdelaername(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifydealername(i)
            #print("Info: Tested Dealer name existing of i= ", i)
    def testverifyexistingofminmax(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygameminmax(i)
    def testVerifyGameTileDisplaysAvailableSeatsForBlackjack(self):

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        for i in range(1, gamecount ):
            gamename = rg_page_obj.returngamename(i)
            print("Debug=",gamename[:16])
            if (gamename[:16] == "Live Common Draw"):
                continue

            gname = rg_page_obj.verifyavailableseats(i)
            print("i=",i)
            if(gname==0):
                print("Bug  for Not availablity of Game Tile Display Seat available: Element= ", i)
                rg_page_obj.appendtofile(1, "Bug  for Not availablity of Game Tile Display Seat available: Game=  " + str(i))

    #Verify Seats Available Update On Evolution Blackjack During Navigation of The Lobby
    def testVerifySeatsAvailableUpdateOnEvolutionBlackjackDuringNavigationofTheLobby(self):  # smart putll test

        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)


        time.sleep(1)
        historymainpage = []
        historynewmainpage = []
        bug_mismatch = 0
        for i in range(1, gamecount):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)
            if (providername != 0):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseats(i)
                historymainpage.append(historyseat)
            if (providername == 0 ):
                continue

        print("historymainpage =", historymainpage)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)
        rg_page_obj.liveblackjack()
        for i in range(1, deductedimage+1):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)
            if (providername != 0 ):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseats(i)
                historynewmainpage.append(historyseat)
            if (providername == 0 ):
                continue
        if (historymainpage != historynewmainpage):
            print(" ")
            print("Info: numbers in main page and landing pager are matching game_num=", i)
                # print("Info: numbers in main page and landing pager are matching game_num=",i)
        if (historymainpage == historynewmainpage):
            print("Bug: Blackjack Games Page numbers in main page after naviagation are not ubdated game_num=", i)
            rg_page_obj.appendtofile(1,"Bug: BlackJack Page numbers in main page after naviagation are not ubdated @testVerifySeatsAvailableUpdateOnEvolutionBlackjackDuringNavigationofTheLobby game_num=" + str(i))
            print("historymainpage=", historymainpage)
            rg_page_obj.appendtofile(1, "historymainpage=" + str(historymainpage))
            print("historylandingpage=", historynewmainpage)
            rg_page_obj.appendtofile(1, "historylandingpage=" + str(historynewmainpage))

    def testVerifySeatsAvailableUpdateOnNetEntBlackjackDuringNavigationofTheLobby(self):  # smart putll test

            rg_page_obj = LiveblackjackPage(self.driver)
            rg_page_obj.liveblackjack()
            ng = rg_page_obj.getgamenumber()
            deductedimage = rg_page_obj.getdeductedimage()
            if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
                ng = 12

            gamecount = rg_page_obj.numberofexistinggamewithname()
            print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
            rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
            time.sleep(1)


            time.sleep(1)
            historymainpage = []
            historynewmainpage = []
            bug_mismatch = 0
            for i in range(1, gamecount):
                providername = rg_page_obj.verifyproviderlogname(i)
                if (providername == 0):  # We need to add game names here based on games added here or modify our current datahook naming
                    historyseat = rg_page_obj.verifyupdateseats(i)
                    historymainpage.append(historyseat)
                if (providername != 0):
                    continue

            print("historymainpage =", historymainpage)
            rg_page_obj.navaigatetofeaturepage()
            time.sleep(60)
            rg_page_obj.liveblackjack()
            for i in range(1, deductedimage):  # footer images are deducted (- 5)
                providername = rg_page_obj.verifyproviderlogname(i)
                if (providername == 0):  # We need to add game names here based on games added here or modify our current datahook naming
                    historyseat = rg_page_obj.verifyupdateseats(i)
                    historynewmainpage.append(historyseat)
                if (providername != 0):
                    continue
            if (historymainpage != historynewmainpage):
                print(" ")
                print("Info: numbers in main page and landing pager are matching game_num=", i)
                # print("Info: numbers in main page and landing pager are matching game_num=",i)
            if (historymainpage == historynewmainpage):
                print("Bug: Blackjack Games Page numbers in main page after naviagation are not ubdated For NetEnt games game=", i)
                rg_page_obj.appendtofile(1,
                                         "Bug: BlackJack Page numbers in main page after naviagation For NetEnt games are not ubdated @testVerifySeatsAvailableUpdateOnNetEntBlackjackDuringNavigationofTheLobby game_num_page=" + str(i))
                print("historymainpage=", historymainpage)
                rg_page_obj.appendtofile(1, "historymainpage=" + str(historymainpage))
                print("historylandingpage=", historynewmainpage)
                rg_page_obj.appendtofile(1, "historylandingpage=" + str(historynewmainpage))
        #Verify Seats Available Update On Netent Blackjack During Navigation of The Lobby

        # Verify Seats Available On Blackjack Evolution Update on Landing Page During Navigation

    def testVerifySeatsAvailableOnBlackjackEvolutionUpdateonLandingPageDuringNavigation(self):  # smart putll test
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        historylandingpage = []
        historynewlandingpage = []
        bug_mismatch = 0
        for i in range(1, gamecount):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)
            if (providername != 0):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseatslandingpage(i)
                historylandingpage.append(historyseat)
            if (providername == 0):
                continue

        print("historymainpage =", historylandingpage)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)
        rg_page_obj.liveblackjack()
        for i in range(1, deductedimage+1):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)
            if (providername != 0):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseatslandingpage(i)
                historynewlandingpage.append(historyseat)
            if (providername == 0):
                continue
        if (historylandingpage != historynewlandingpage):
            print(" ")
            print("Info: numbers in landing pager are updated")
            print(" historylandingpage=", historylandingpage)
            print(" str(historynewlandingpage=", historynewlandingpage)
            # print("Info: numbers in main page and landing pager are matching game_num=",i)
        if ( historylandingpage == historynewlandingpage):
            print("Bug: Blackjack Games Page numbers in landing page after naviagation are not ubdated game_num=", i)
            rg_page_obj.appendtofile(1,"Bug: BlackJack Page numbers in landing page after naviagation are not ubdated @testVerifySeatsAvailableOnBlackjackEvolutionUpdateonLandingPageDuringNavigation game_num=" + str(i))
            print(" historylandingpage=",  historylandingpage)
            rg_page_obj.appendtofile(1, " historylandingpage=" + str(historylandingpage))
            print("historylandingpage=", historylandingpage)
            rg_page_obj.appendtofile(1, "historynewlandingpage=" + str(historynewlandingpage))

    def testVerifySeatsAvailableOnBlackjackNetEntUpdateonLandingPageDuringNavigation(self):  # smart putll test
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        historylandingpage = []
        historynewlandingpage = []
        bug_mismatch = 0
        for i in range(1, gamecount):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)
            print("providername=",providername)
            if (providername != 0):
                continue
            print("i_netent=",i)

            gamename =rg_page_obj.returngamename(i)
            if (gamename[:16] !="Live Common Draw" and gamename !="Live Blackjack Common Draw Low Roller HTML5"):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseatslandingpage(i)
                historylandingpage.append(historyseat)

#Live Blackjack Common Draw Low Roller HTML5
        print("historyLanding pageNetEnt =", historylandingpage)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)
        rg_page_obj.liveblackjack()
        for i in range(1, deductedimage+1):  # footer images are deducted (- 5)
            providername = rg_page_obj.verifyproviderlogname(i)#after recent change in UI 0 meand NetEnt, u'' means Evo
            gamename = rg_page_obj.returngamename(i)
            if (providername == 0  and gamename[:16] !="Live Common Draw"):  # We need to add game names here based on games added here or modify our current datahook naming
                historyseat = rg_page_obj.verifyupdateseatslandingpage(i)
                historynewlandingpage.append(historyseat)

        if (historylandingpage != historynewlandingpage):
            print(" ")
            print("Info: numbers in landing pager are updated")
            print(" historylandingpage=", historylandingpage)
            print(" str(historynewlandingpage=", historynewlandingpage)
            # print("Info: numbers in main page and landing pager are matching game_num=",i)
        if ( historylandingpage == historynewlandingpage):
            print("Bug: Blackjack Games Page numbers in landing page after naviagation are not ubdated For NetEng Games game_num=", i)
            rg_page_obj.appendtofile(1,"Bug: BlackJack Page numbers in landing page after naviagation are not ubdated @testVerifySeatsAvailableOnBlackjackNetEntUpdateonLandingPageDuringNavigation game_num=" + str(i))
            print(" historylandingpage=",  historylandingpage)
            rg_page_obj.appendtofile(1, " historylandingpage=" + str(historylandingpage))
            print("historylandingpage=", historylandingpage)
            rg_page_obj.appendtofile(1, "historynewlandingpage=" + str(historynewlandingpage))


    def testVerify_A_User_Can_Sort_Blackjack_Name_Descending_By_Clicking_text_ZAtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,1)#1 means using text for sorting

    def testVerify_A_User_Can_Sort_Blackjack_Name_Ascending_By_Clicking_text_AZtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Blackjack_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,2)#2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Blackjack_Name_By_Displayed_Ascending_Arrowtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,2)#2 means using arrow for sorting

    def testVerify_A_User_Can_Sort_Blackjack_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount, 2)  # 2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Blackjack_Stake_Size_Descending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Blackjack_Stake_Size_Ascending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,1)#1 means using text for sorting


     #Sorting by arrow directions


    def testVerify_A_User_Can_Sort_Blackjack_Stake_Size_Descending_By_Clicking_Arrow_Uptest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_A_User_Can_Sort_Blackjack_Stake_Size_Ascending_By_Clicking_Arrow_Downtest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_Refreshing_Blackjack_Page_Display_Default_Assending_Sort_by_Game_Namestest(self):
        rg_page_obj = LiveblackjackPage(self.driver)
        rg_page_obj.liveblackjack()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(BlackJack) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(BlackJack) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount, 1)  # 1 means using text for sorting

        #gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount, 2)  # 2 means using arrow for sorting
    def testVerify_Sort_Arrow_is_existing_in_Blackjack_Pagetest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(6)  # existing of sort arrow
    def testVerify_text_Sortby_is_existing_in_Blackjack_Pagetest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(5)  #
        print(name)
        if (name == 'Sort by:'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "BlackJack Game Stake Size text is existing:")

    def testVerify_text_StakeSize_is_existing_in_Blackjack_Pagetest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(4)  #
        print(name)
        if (name == 'Stake Size'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "BlackJack Game Stake Size text is existing:")

    def testVerify_text_ZA_changes_to_AZ_by_clicking_in_Blackjack_Pagetest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(3)  #
        print(name)
        if (name == 'A-Z'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "BlackJack Game Z-A changes to A-Z for sorting:")

    def testVerify_text_AZ_changes_to_ZA_by_clicking_in_Page_Blackjacktest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(2)  #
        print(name)
        if (name == 'Z-A'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "BlackJack Game A-Z changes to Z-A for sorting:")

    def testVerify_text_AZ_is_existing_in_Blackjack_Pagetest(self):
        bj_page_obj = LiveblackjackPage(self.driver)
        bj_page_obj.liveblackjack()
        name = bj_page_obj.pageverificationelementexisting(1)#1 means verify exising of A-z
        print(name)
        if(name=='A-Z'):
            print("Pass!")
            bj_page_obj.appendtofile(2,"BlackJack Game A-Z existing for sorting:")
    def tearDown(self):
        print("liveblackjacktest:ended")
        sg_page_obj = LiveblackjackPage(self.driver)
        sg_page_obj.appendtofile(2, "BlackJack Game Finished Testing: ")
        sg_page_obj.appendtofile(2, str(datetime.datetime.now()))
        #sg_page_obj.appendtofile(1, "Finished Testing:  ")
        #sg_page_obj.appendtofile(1, str(datetime.datetime.now()))
        super(liveblackjacktest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()