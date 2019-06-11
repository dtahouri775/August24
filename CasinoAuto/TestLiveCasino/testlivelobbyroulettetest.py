'''
Created on December 11, 2018
Change on December 22, 2018
@author: Daryoush
Change on January 24, 2019
Change on February 13, 2019
'''
import unittest
import nose
import time

from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.LiveRoulettePage  import LiveroulettePage
import datetime


class liveroulettetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(liveroulettetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()
        print("liveroulettete:Starts")
        sg_page_obj = LiveroulettePage(self.driver)
        sg_page_obj.appendtofile(2, "Liveroulette Game Started: ")
        sg_page_obj.appendtofile(2, str(datetime.datetime.now()))
    def testVerify_A_User_Can_Direct_Launch_RouletteTest(self):

            lg_page_obj = LiveroulettePage(self.driver)
            lg_page_obj.liveroulette()
            ng = lg_page_obj.getgamenumber()
            deductedimage = lg_page_obj.getdeductedimage()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            gamecount = lg_page_obj.numberofexistinggamewithname()
            print("Info: Number of games in this(Roulette) page equals: ", gamecount)
            lg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
            time.sleep(1)

            for i in range(1, gamecount):
                #print('Info i= ',i)
                lg_page_obj.nothanks()
                exist=lg_page_obj.existgameimage(i)
                if (exist == 1):
                    gname = lg_page_obj.click_loginfromlandingpage(i)
                    lg_page_obj.logout()
                    lg_page_obj.nothanks()
                if (exist == 0):
                    lg_page_obj.appendtofile(1, "Bug:GameImage In Roulette Page Does not exist:  gname=: " + str(i))
                    print("Bug:GameImage In Roulette Page Does not exist:  gname=", i)
                    #k = k + 1



    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifylandingpageinfo(i)
            print("Info: Verify landing page in Roulette games for the required information i= ", i)
            rg_page_obj.appendtofile(2, "Info: Number of games in this page equals ng =" + str(i))

    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyproviderlog(i)
            print("Info: existing In Roulette page log of i= ", i)
            rg_page_obj.appendtofile(2, "Info: Existing in Roulette page log of  i=" + str(i))

    def testverifyexistingofgamename(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygamename(i)
            print("Info: In Roulette Page Game existing of i= ", i)
            rg_page_obj.appendtofile(2, "Info: In Roulette Page Game existing of i=" + str(i))

    def testverifyexistingofdelaername(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        #print("Number of images in this page equals: ", ng)
        print("Info:Number of Games in Roulette page equals: ", deductedimage)
        rg_page_obj.appendtofile(2, "Info Number of games in Roulette page equals: ng =" + str(deductedimage))
        time.sleep(1)
        for i in range(1, deductedimage+1):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifydealername(i)
            if (gname == 1):
                print("Info: Dealer name In Roulette Page existing of i= ", i)
                rg_page_obj.appendtofile(2, "Info: Dealer name In Roulette Page existing of i=" + str(i))
            if (gname == 0):
                print("Bug: Dealer name in Roulette page is not existing  of i= ", i)
                rg_page_obj.appendtofile(1, "Bug: Dealer name in Live Roulette page is not existing(Make sure is not auto roulette)  game=" + str(i))

    def testverifyexistingofminmax(self):

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifygameminmax(i)
            if (gname == 1):
                print("Info Roulette Page : Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(2, "Info:Roulette Min-Max existing of i=" + str(i))
            if (gname == 0):
                print("Bug: Roulette Page NOt Existing of min-max  i= ", i)
                rg_page_obj.appendtofile(1, "Info: Roulette Page Not existing of min-max i=" + str(i))
    def testVerifyGameTileDisplayslaysLastResultsForRoulette(self):

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)

        for i in range(1, gamecount):
            gname = rg_page_obj.verifyavailablenumbers(i)

    '''
    def testVerifyRouletteResultsUpdateDuringNavigationOfTheLobbyForEvo(self):#smart putll test

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        oldhistory =[]
        for i in range(1, gamecount):
            providerlog = rg_page_obj.verifyproviderlogname(i)
            if (providerlog != 0):
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                oldhistory.append(historymainpage)
        rg_page_obj.navaigatetofeaturepage()
        print("oldhistory =", oldhistory)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(60)  # wait for 60 second to make sure the results will be updated
        rg_page_obj.liveroulette()#return to roulette page
        newhistorymainpage = []
        newhistory = []
        for i in range(1, deductedimage+1):  # -7 just in case some of the games has been removed
            providerlog = rg_page_obj.verifyproviderlogname(i)
            if(providerlog!=0):
                newhistorymainpage = rg_page_obj.verifyavailablenumbers(i)
                newhistory.append(newhistorymainpage)
            #print("newhistorymainpage=", newhistorymainpage)
        print("newhistory =",newhistory )
        compar_result=cmp(newhistory,oldhistory)
        print(" compar_result =",  compar_result)
        if(compar_result==0):
            print("Bug Failure: None of the game history result are updated For Evolution games!")
            rg_page_obj.appendtofile(1, "Bug Failure: Roulette Page None of the game history result are updated For Evolution games!")
            print("newhistory = ", newhistory)
            rg_page_obj.appendtofile(1,"newhistory ="+str(newhistory))
            print("oldhistory = ", oldhistory)
            rg_page_obj.appendtofile(1, "oldhistory =" + str(oldhistory))

        if(compar_result != 0):
            print("info: Pass the test: VerifyRouletteResultsUpdateDuringNavigationOfTheLobbyEvo")
            rg_page_obj.appendtofile(2,"info: Pass the test: VerifyRouletteResultsUpdateDuringNavigationOfTheLobbyEvo")

    '''
    def testVerifyRouletteResultsUpdateDuringNavigationOfTheLobbyForNetEntAndEvo(self):#smart putll test

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        oldhistory = []
        for i in range(1, gamecount):
            providerlog = rg_page_obj.verifyproviderlogname(i)
            #if (providerlog == 0):#may I need to modify this portion
            historymainpage = rg_page_obj.verifyavailablenumbers(i)
            oldhistory.append(historymainpage)
        rg_page_obj.navaigatetofeaturepage()
        print("oldhistory =", oldhistory)
        rg_page_obj.navaigatetofeaturepage()
        time.sleep(1)  # wait for 60 second to make sure the results will be updated
        rg_page_obj.liveroulette()#return to roulette page
        newhistorymainpage = []
        newhistory = []
        for i in range(1, deductedimage+1):  # -7 just in case some of the games has been removed
            providerlog = rg_page_obj.verifyproviderlogname(i)
            if(providerlog==0):
                newhistorymainpage = rg_page_obj.verifyavailablenumbers(i)
                newhistory.append(newhistorymainpage)
            #print("newhistorymainpage=", newhistorymainpage)
        print("newhistory =",newhistory )
        compar_result=cmp(newhistory,oldhistory)
        print(" compar_result =",  compar_result)
        if(compar_result==0):
            print("Bug Failure: None of the game history NetEnt results are updated! Make sure NetEnt has game in Roulette page!!")
            rg_page_obj.appendtofile(1, "Bug Failure: None of the game history NetEnt results are updated! Make sure NetEnt has game in Roulette page!!")
            print("newhistory_NetEnt = ", newhistory)
            rg_page_obj.appendtofile(1,"newhistory_NetEnt = "+str(newhistory))
            print("oldhistory_NetEnt = ", oldhistory)
            rg_page_obj.appendtofile(1, "oldhistory_NetEnt = " + str(oldhistory))
        if(compar_result != 0):
            print("info: Pass the test: VerifyRouletteResultsUpdateDuringNavigationOfTheLobby NeEng")
            rg_page_obj.appendtofile(2,"Pass the test: VerifyRouletteResultsUpdateDuringNavigationOfTheLobby NeEng")

    '''
    def testVerifyEvolutionRouletteResultsUpdateonLandingPageDuringNavigation(self):#smart putll test

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        numevo = 0
        bug_mismatch =0
        for i in range(15, gamecount):

            providerlog = rg_page_obj.verifyproviderlogname(i)
            if (providerlog == 0):  # 0 means Netent
                continue
            if (providerlog != 0):#0 means Netent
               numevo=numevo+1
            historymainpage = rg_page_obj.verifyavailablenumbers(i)
            #print("historymainpage=",historymainpage)
            historylandingpage = rg_page_obj.verifyavailablenumberslandingpage(i)
            #print("historylandingpage=", historylandingpage)
            if(historymainpage==historylandingpage):
                print("G= ",i)
                #print("Info: numbers in main page and landing pager are matching game_num=", i)
                #print("Info: numbers in main page and landing pager are matching game_num=",i)
            if (historymainpage != historylandingpage):
                # one more time taken updated number from main page
                historymainpage = rg_page_obj.verifyavailablenumbers(i)
                if (historymainpage == historylandingpage):
                    print("Info: numbers in main page and landing pager are matching after second trygame_num=", i)
                    rg_page_obj.appendtofile(2,"Info: numbers in main page and landing pager are matching after second trygame_num=" + str(i))
                    continue
                print("Bug: Evo games numbers in main page and landing pager are not matching game_num=", i)
                rg_page_obj.appendtofile(1, "Bug: Evo games numbers in main page and landing pager are not matching game_num="+ str(i))
                print("historymainpage=", historymainpage)
                rg_page_obj.appendtofile(1,"historymainpage=" + str(historymainpage))
                print("historylandingpage=", historylandingpage)
                rg_page_obj.appendtofile(1, "historylandingpage=" + str(historylandingpage))
                bug_mismatch=bug_mismatch+1#for any mismatch
        if(bug_mismatch>.8*numevo):
            print("Bug Failure: Roulette Page > more than 80% of evo games number between front page and landing page are not matching! ")
            rg_page_obj.appendtofile(1, "Bug Failure: Roulette Page > more than 80% of evo games number between front page and landing page are not matching! ")
            print("numevo=",numevo)
            rg_page_obj.appendtofile(1,"numevo=", numevo)

        if (bug_mismatch <= .8 * numevo):
            print("Info Pass: Roulette Page > more than 80% of evo games number between front page and landing page are matching! ")
            rg_page_obj.appendtofile(2, "Info Pass: Roulette Page > more than 80% of evo games number between front page and landing page are matching! ")
            print("numevo=", numevo)
            rg_page_obj.appendtofile(2,"numevo="+str(numevo))

    '''
    def testVerifyNetentAndEvoRouletteResultsUpdateonLandingPageDuringNavigation(self):#smart putll test

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        numnetent = 0
        bug_mismatch = 0
        #for i in range(6, 7):
        for i in range(1, gamecount):
            providerlog = rg_page_obj.verifyproviderlogname(i)
            #if (providerlog != 0):#Evo is u ''
             #   continue
            #if (providerlog == 0):
             #  numnetent=numnetent+1
            historymainpage = rg_page_obj.verifyavailablenumbers(i)
            historylandingpage = rg_page_obj.verifyavailablenumberslandingpage(i)
            if(historymainpage==historylandingpage):
                print("Info: numbers in main page and landing pager are matching game_num=",i)
                rg_page_obj.appendtofile(2,"Info: numbers in main page and landing pager are matching game_num="+str(i))
                continue
            if (historymainpage != historylandingpage and historymainpage !=-1 ):
                historymainpage = rg_page_obj.verifyavailablenumbers(i)  # one more time taken updated number from main page
                if (historymainpage == historylandingpage):
                    print("Info: numbers in main page and landing pager are matching after second trygame_num=", i)
                    rg_page_obj.appendtofile(2,"Info: numbers in main page and landing pager are matching after second trygame_num=" + str(i))
                    continue
                print("Bug: @testVerifyNetentRouletteResultsUpdateonLandingPageDuringNavigation NetEnt games numbers in main page and landing pager are not matching game_num=", i)
                rg_page_obj.appendtofile(1,"Bug: @VerifyNetentRouletteResultsUpdateonLandingPageDuringNavigationNetEnt games numbers in main page and landing pager are not matching game_num=" + str(i))
                print("historymainpage=", historymainpage)
                rg_page_obj.appendtofile(1,"historymainpage=" + str(historymainpage))
                print("historylandingpage=", historylandingpage)
                rg_page_obj.appendtofile(1, "historymainpage=" + str(historylandingpage))
                bug_mismatch=bug_mismatch+1#for any mismatch
        if(bug_mismatch>.8*numnetent):
            print("Bug Failure: Roulette Page > more than 80% of NetEnt games number between front page and landing page are not matching! ")
            rg_page_obj.appendtofile(1, "Bug Failure: Roulette Page > more than 80% of NetEnt games number between front page and landing page are not matching! ")
        if (bug_mismatch <= .8 * numnetent):
            print("Info Pass: Roulette Page > more than 80% of NetEnt games number between front page and landing page are matching! ")
            rg_page_obj.appendtofile(2, "Info Pass: Roulette Page > more than 80% of NetEnt games number between front page and landing page are matching! ")

    def testVerify_A_User_Can_Sort_Roulette_Name_Descending_By_Clicking_text_ZAtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,1)#1 means using text for sorting

    def testVerify_A_User_Can_Sort_Roulette_Name_Ascending_By_Clicking_text_AZtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Roulette_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount,2)#2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Roulette_Name_By_Displayed_Ascending_Arrowtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount,2)#2 means using arrow for sorting

    def testVerify_A_User_Can_Sort_Roulette_Name_By_Displayed_Descending_Arrowtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortZA(gamecount, 2)  # 2 means using arrow for sorting


    def testVerify_A_User_Can_Sort_Roulette_Stake_Size_Descending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,1)#1 means using text for sorting
    def testVerify_A_User_Can_Sort_Roulette_Stake_Size_Ascending_By_Clicking_Stake_Size_Text(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,1)#1 means using text for sorting


     #Sorting by arrow directions


    def testVerify_A_User_Can_Sort_Roulette_Stake_Size_Descending_By_Clicking_Arrow_Uptest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymaxtexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_A_User_Can_Sort_Roulette_Stake_Size_Ascending_By_Clicking_Arrow_Downtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount -1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount -1 ))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount,2)#2 means using arrow for sorting
    def testVerify_Refreshing_Roulette_Page_Display_Default_Assending_Sort_by_Game_Namestest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        deductedimage = rg_page_obj.getdeductedimage()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        time.sleep(1)
        gamecount = rg_page_obj.numberofexistinggamewithname()
        print("Info: Number of games in this(Roulette) page equals: ", gamecount - 1)
        rg_page_obj.appendtofile(2, "Info: Number of games in this(Roulette) page equals: " + str(gamecount - 1))
        time.sleep(1)
        gname = rg_page_obj.verifycorrectSortAZ(gamecount, 1)  # 1 means using text for sorting

        #gname = rg_page_obj.verifycorrectSortStakesizebymintexttry(gamecount, 2)  # 2 means using arrow for sorting
    def testVerify_Sort_Arrow_is_existing_in_Roulette_Pagetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(6)  # existing of sort arrow
    def testVerify_text_Sortby_is_existing_in_Roulette_Pagetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(5)  #
        print(name)
        if (name == 'Sort by:'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Roulette Game Stake Size text is existing:")

    def testVerify_text_StakeSize_is_existing_in_Roulette_Pagetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(4)  #
        print(name)
        if (name == 'Stake Size'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Roulette Game Stake Size text is existing:")

    def testVerify_text_ZA_changes_to_AZ_by_clicking_in_Roulette_Pagetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(3)  #
        print(name)
        if (name == 'A-Z'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Roulette Game Z-A changes to A-Z for sorting:")

    def testVerify_text_AZ_changes_to_ZA_by_clicking_in_Page_Roulettetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(2)  #
        print(name)
        if (name == 'Z-A'):
            print("Pass!")
        bj_page_obj.appendtofile(2, "Roulette Game A-Z changes to Z-A for sorting:")

    def testVerify_text_AZ_is_existing_in_Roulette_Pagetest(self):
        bj_page_obj = LiveroulettePage(self.driver)
        bj_page_obj.liveroulette()
        name = bj_page_obj.pageverificationelementexisting(1)#1 means verify exising of A-z
        print(name)
        if(name=='A-Z'):
            print("Pass!")
            bj_page_obj.appendtofile(2,"Roulette Game A-Z existing for sorting:")
    def tearDown(self):
        print("liveroulettete:ended")
        super(liveroulettetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()