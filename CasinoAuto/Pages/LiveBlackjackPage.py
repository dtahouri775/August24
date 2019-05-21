'''
Created on December 11, 2018
Changed on December 20
@author: Daryoush
Moddified on December 11
'''
from BasePage import BasePage
from CasinoAuto.Constants               import Casino_Constants
from CasinoAuto.Locators.UIMapLiveCasino import Livegamescommon
from CasinoAuto.Locators.UIMapLiveCasino import LivegamenameMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameDealernameMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameminmaxMap
from CasinoAuto.Locators.UIMapLiveCasino import LiveInfoPageMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameImagePageMap
#LivegameImagePageMap
import time
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
#from CasinoAuto.Locators.UIMapLiveCasino import LiveblackjackPageMap
from MatchBookLoginPage import MatchBookLoginPage
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath
from CasinoAuto.Locators.UIMapCasinoPage import CasinoPageMapXpath
from CasinoAuto.Locators.UIMapLiveCasino import LiveGameSeatavailableMap
from CasinoAuto.Locators.UIMapLiveCasino import LandingpageSeatavailableMap
from CasinoAuto.Locators.UIMapLiveCasino import LiveProviderLogNameMap
import datetime
import re
from re import sub
from decimal import Decimal
class LiveblackjackPage(BasePage):
    def __init__(self, driver):
        super(LiveblackjackPage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum

        gamenum = len(webElementsList)
        global deductedimage
        deductedimage=gamenum-23#8 may be modified based on modification on this page
        #deductedimage= self.numberofexistinggamewithname()
        self.appendtofile(2,"Total Number of images in Blackjack games = "+str(gamenum))
    # defining the casino page object here
        try:
            element = self.find_element("cssSelector", LiveCasinoPageMap["AcceptCookies"])
            element.click()
        except:
            print("Live Black Jack Page: Cookies dialog box is not there Element=")

    def _verify_page(self):
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()


            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBlackjack"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveBlackjack"])
            element1.click()

        except:
            raise Exception("LiveLiveBlackjack locator or livecasinoLocatortop is not accessable")

    def liveblackjack(self):
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBlackjack"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveBlackjack"])
        element1.click()

    def getgamenumber(self):
        return gamenum
    def getdeductedimage(self):
        return deductedimage
    def click_loginfromlandingpage(self, a):



            mainWindowHandle = self.driver.window_handles
            self.click(10,
                       "xpath",
                       LogInPageMap['LogInToMatchbookTextXpath']
                       )
            allWindowHandles = self.driver.window_handles
            for handle in allWindowHandles:
                if handle != mainWindowHandle[0]:
                    self.switch_to_window(handle)
                    break
            log_obj = MatchBookLoginPage(self.driver,
                                         Casino_Constants['CAsino_Username'],
                                         Casino_Constants['Casino_Password']
                                         )
            log_obj.login()
            try:
                self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["rhsaccount"])
                element = self.find_element("cssSelector", CasinoPageMapXpath["rhsaccount"])
                element.click()
                time.sleep(2)
                self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["Usernametitle"])
                element = self.find_element("cssSelector", CasinoPageMapXpath["Usernametitle"])
                text1 = element.text
                print(text1)
                self.appendtofile(2,"BalckjackPage element righ hand navigation is displayed after successful log in!")

                if (text1 !=""):
                    print(" ")
                    #print("Info: Successful Log in")

            except:
                self.appendtofile(1,"Bug: Either username or  righ hand navigation is displayed after successful log in! game="+str(a))
                raise Exception(" user name is not displayed")

            tempng1 = "LiveGameimage" + str(a)
            try:#click game image again after logged in to load the game
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameImagePageMap[tempng1])
                element1 = self.find_element("cssSelector", LivegameImagePageMap[tempng1])
                try:
                    element1.click()
                    return 1
                except:
                    self.appendtofile(1,"Bug Live Black Jack Page:Element Livegamelaunch is not clickable yet, probably image is not there! Element="+ str(a))
                    print("Bug Live Black Jack Page:Element Livegamelaunch is not clickable yet, probably image is not there! Element=", a)
                    return 0
            except:
                self.appendtofile(1,"Bug Live Black Jack Page: Element Livegamelaunch is not displayed! Element=" + str(a))
                print("Bug Live Black Jack Page:Element  image in Black jack is not clickable yet, probably image is not there! Element=", a)


            return (text1)
    def nothanks(self):
        try:
            element3 = self.find_element("cssSelector", HomePageMapXpath["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"


    def logout(self):

            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["rhsaccount"])
            element3 = self.find_element("cssSelector", CasinoPageMapXpath["rhsaccount"])
            element3.click()
            time.sleep(2)
            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["Usernametitle"])

            element = self.find_element("cssSelector", CasinoPageMapXpath["Usernametitle"])
            element.click()

            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["logout"])
            element2 = self.find_element("cssSelector", CasinoPageMapXpath["logout"])
            element2.click()
            time.sleep(5)
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBlackjack"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveBlackjack"])
            element1.click()

    def verifylandingpageinfo(self,a):
        er=0
        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveInfoPageMap[tempng1])
        element1 = self.find_element("cssSelector", LiveInfoPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:

            element1.click()
        except:
            self.appendtofile(1,"Bug Live Black Jack Page: Not able to click  <i> button, may be covered by bet slip Bug  i: element->"+str(a))
            print("Bug Live Black Jack Page: Not able to click  <i> button, may be covered by bet slip Bug  i: element->",a)
            er=1

        if(er==0):#if accessed to landing page

            #verify game name
            try:
                gamename = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgname"])
                gamename = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgname"])
                text = gamename.text
                #print("Info Live Black Jack: gamename",text)
            except:
                self.appendtofile(1, "Bug Live Black Jack Page:Game Name is not available  game = " + str(a))
                print("Bug Live Black Jack Page:Game Name is not available ")
            #verify game provider
            try:
                gameprovider = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPprovider"])
                gameprovider = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPprovider"])

            except:
                self.appendtofile(1, "Bug:Game Provider is not available  game = " + str(a))
                raise Exception("Bug:Game Provider is not available:  Elemnent=",a)

            #verify game rule is there
            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgamerule"])
                gamerule = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgamerule"])

            except:
                self.appendtofile(1, "Bug Game Rule is not available  game = " + str(a))
                raise Exception("Bug Game Rule is not available  GameElement=",a)

                # verify game description is there
            try:
                gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                text = gamedes.text
                #print("Info: Game description is:",text)
            except:
                self.appendtofile(1, "Bug Live Black Jack Page: Game Descritpin is not available  game = " + str(a))
                print("Bug Live Black Jack Page:Bug Game Descritpin is not available  gamenum=", a)

            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePlaynow"])
                gamerule = self.find_element("cssSelector", LiveCasinoPageMap["LivePlaynow"])
                #print("Info: Live Play now is displayed")
            except:
                self.appendtofile(1, "Exception Failure Bug in LivePlaynow is not available!!   " )
                raise Exception("Exception Bug in LivePlaynow is not available ")

            #LivePlaynow
            element2 = self.find_element("cssSelector", Livegamescommon["Livebreadcrumbl"])
            element2.click()
            time.sleep(1)


    def existgameimage(self,a):
        tempng1 = "LiveGameimage" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameImagePageMap[tempng1])
            element1 = self.find_element("cssSelector", LivegameImagePageMap[tempng1])
            try:
                element1.click()
                return 1
            except:
                self.appendtofile(1, "Bug Live Black Jack Page:Element is not clickable yet, probably image is not there! Element="+str(a))
                print("Bug Live Black Jack Page:Element is not clickable yet, probably image is not there! Element=",a)
                return 0

        except:
            self.appendtofile(1,"Bug Live Black Jack Page:Element is not displayed, probably image is not there at all! game=" + str(a))
            print("Bug Live Black Jack Page:Element is not displayed, probably image is not there at all! Element=", a)
            return 0
    def verifyproviderlog(self,a):
        tempng1 = "ProviderLog" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap[tempng1])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap[tempng1])
            try:
                #print("Info: Assumption is all the images are there")
                return 1
            except:
                self.appendtofile(1,"Bug Live Black Jack Page:ProviderLog is not there!! game=" + str(a))
                print("Bug Live Black Jack Page:ProviderLog is not there!")
                return 0

        except:
            return 0
    def verifyproviderlogname(self,a):
        tempng1 = "ProviderName" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveProviderLogNameMap[tempng1])
            element1 = self.find_element("cssSelector", LiveProviderLogNameMap[tempng1])
            try:
                #print("Assumption is all the images are there")
                return element1.get_attribute(('id'))
            except:
                print("ProviderLog is not there!")
                return 0

        except:
            return 0

    # live game name under images
    def verifygamename(self,a):
        tempng1 = "Livegname" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng1])
            element1 = self.find_element("cssSelector", LivegamenameMap[tempng1])
            return element1.text
        except:
            self.appendtofile(1, "Bug Live Black Jack Page:game name is not there!! game=" + str(a))
            print("Bug Live Black Jack Page:Game name is not there! Elemnent= ", a)
            return 0

        return 0
    def numberofexistinggamewithname(self):#maximum 200 games per page in this version
        for i in range(1, 201):
            tempng1 = "Livegname" + str(i)
            try:
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng1])
                element1 = self.find_element("cssSelector", LivegamenameMap[tempng1])
            except:
                return i

    #verifygame min-max existing next to info icon

    def verifygameminmax(self,a):
        tempng1 = "Livegminmax" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameminmaxMap[tempng1])
            element1 = self.find_element("cssSelector", LivegameminmaxMap[tempng1])
            return 1;
        except:
            self.appendtofile(1, "Bug Live Black Jack Page:Provider min-max is not there!! game=" + str(a))
            print("Bug Live Black Jack Page:Provider min-max is not there! Element= ",a)
            return 0
    def verifyavailableseats(self,a):
        tempng1 = "Livegameresult" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon[tempng1])
            element1 = self.find_element("cssSelector", Livegamescommon[tempng1])
            seat = element1.text
            #print("Info Ok, for GameTile Display Seat available:",seat)
            if(seat==''):
                return 0
            return 1;
        except:
            self.appendtofile(1, "Bug Blackjack Page method: verifyavailableseats for Not availablity of Game Seats Display Seat available:!! game=" + str(a))
            print("Bug  for Not availablity of Game Seats Display Seat available: Element= ",a)
            return 0
    def verifyupdateseats(self, a):
        tempng1 = "SeatavailableGamepge" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveGameSeatavailableMap[tempng1])
            element1 = self.find_element("cssSelector", LiveGameSeatavailableMap[tempng1])
            seat = element1.text
            print("Info Ok, for GameTile Display Seat available:", seat)
            self.appendtofile(2, "Info Ok, for GameTile Display Seat available: Element=" + str(a))
            return seat;
        except:
            #self.appendtofile(1, "Bug  for Not availablity of Game Tile Display Seat available: Element=" + str(a))
            #print("Bug  for Not availablity of Game Tile Display Seat available: Element= ", a)
            return -1

    def verifyupdateseatslandingpage(self,a):
        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveInfoPageMap[tempng1])
        element1 = self.find_element("cssSelector", LiveInfoPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:
            element1.click()
        except:
            print("Not able to click  <i> button, may be covered by bet slip Bug  200i: element->", a)
        tempng1 = "SeatnumberLandingpage"
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LandingpageSeatavailableMap[tempng1])
            element1 = self.find_element("cssSelector", LandingpageSeatavailableMap[tempng1])
            seat = element1.text
            print("Info Ok, for GameTile Display Seat available:", seat)
            self.appendtofile(2, "Info Ok, for GameTile Display Seat available: Element=" + str(a))
            element2 = self.find_element("cssSelector",Livegamescommon["Livebreadcrumbl"])  # return to main page of roulette
            element2.click()
            time.sleep(1)
            return seat;
        except:
            # self.appendtofile(1, "Bug  for Not availablity of Game Tile Display Seat available: Element=" + str(a))
            # print("Bug  for Not availablity of Game Tile Display Seat available: Element= ", a)
            return -1
    def verifydealername(self,a):
        tempng1 = "LiveDealername" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameDealernameMap[tempng1])
            element1 = self.find_element("cssSelector", LivegameDealernameMap[tempng1])
            return 1;
        except:
            self.appendtofile(1, "Bug Live Black Jack Page: Dealer name is not there! game=" + str(a))
            print("Bug Live Black Jack Page:Dealer name is not there!  Element=",a)
            return 0

    def verifyupdateseats(self, a):
        tempng1 = "SeatavailableGamepge" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveGameSeatavailableMap[tempng1])
            element1 = self.find_element("cssSelector", LiveGameSeatavailableMap[tempng1])
            seat = element1.text
            print("Info Ok, for GameTile Display Seat available:", seat)
            self.appendtofile(2, "Info Ok, for GameTile Display Seat available: Element=" + str(a))
            return seat;
        except:
            #self.appendtofile(1, "Bug  for Not availablity of Game Tile Display Seat available: Element=" + str(a))
            #print("Bug  for Not availablity of Game Tile Display Seat available: Element= ", a)
            return -1

    def verifyupdateseatslandingpage(self,a):
        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveInfoPageMap[tempng1])
        element1 = self.find_element("cssSelector", LiveInfoPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:
            element1.click()
        except:
            print("Not able to click  <i> button, may be covered by bet slip Bug  200i: element->", a)
        tempng1 = "SeatnumberLandingpage"
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LandingpageSeatavailableMap[tempng1])
            element1 = self.find_element("cssSelector", LandingpageSeatavailableMap[tempng1])
            seat = element1.text
            print("Info Ok, for GameTile Display Seat available:", seat)
            self.appendtofile(2, "Info Ok, for GameTile Display Seat available: Element=" + str(a))
            element2 = self.find_element("cssSelector",Livegamescommon["Livebreadcrumbl"])  # return to main page of roulette
            element2.click()
            time.sleep(1)
            return seat;
        except:
            # self.appendtofile(1, "Bug  for Not availablity of Game Tile Display Seat available: Element=" + str(a))
            # print("Bug  for Not availablity of Game Tile Display Seat available: Element= ", a)
            return -1

    def navaigatetofeaturepage(self):
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveLobby"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveLobby"])
            element1.click()
            return 1
        except:
            print("Can not navaigate to featurepage")
            return 0

    def returngamename(self, a):
        tempng1 = "Livegname" + str(a)
        try:
            if(a==2):
                print("Debug me here!!")
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng1])
            element1 = self.find_element("cssSelector", LivegamenameMap[tempng1])
            gname = element1.get_attribute('innerText')
            return gname
        except:
            self.appendtofile(1, "Bug BlackJack page Can not return game name! Livegname=" + str(a))
            print("Bug BlackJack page was not able to return game name=", tempng1)
            return 0
    def verifycorrectSortZA(self, a,option):
        try:
            if(option==1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                self.az.click()  # make A-Z active
            #Livesortnamebyarrowdesc
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortnamebyarrowasc"])
                self.arrow.click()  # make A-Z active
            for i in range(1, a - 1):  # footer images are deducted (- 5)
                tempng1 = "Livegname" + str(i)
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng1])
                element1 = self.find_element("cssSelector", LivegamenameMap[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "Livegname" + str(i + 1)
                element2 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng2])
                element2 = self.find_element("cssSelector", LivegamenameMap[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                sortresult = self.comparealphanumeric(text1, text2)
                if (cmp(text1, text2) == 0):
                    sortresult = 0
                if (sortresult == -1 or sortresult == 0):
                    print("Pass")
                else:
                    self.appendtofile(1,
                                      "Faiure Bug in Blackjack Page: Z-A sorting is not quite functioning correctly")
                    raise Exception("A-Z sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in BlackJack Page: Z-A sorting is not displayed for clicking")
            raise Exception("Z-A sorting is not  displayed for clicking")

    def verifycorrectSortAZ(self, a,option):
        try:
            if(option==1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",Livegamescommon["Livesortnamebyarrowasc"])
            # self.az.click()  # make A-Z active
            for i in range(1, a - 1):  # footer images are deducted (- 5)
                tempng1 = "Livegname" + str(i)
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng1])
                element1 = self.find_element("cssSelector", LivegamenameMap[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "Livegname" + str(i + 1)
                element2 = self.wait_for_element_visibility(10, "cssSelector", LivegamenameMap[tempng2])
                element2 = self.find_element("cssSelector", LivegamenameMap[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                sortresult = self.comparealphanumeric(text1,text2)
                if (cmp(text1, text2) == 0):
                    sortresult = 0
                if (sortresult == 1 or sortresult == 0):
                    print("Pass")
                else:
                    self.appendtofile(1,"Failure Bug in BlackJack Page: A-Z sorting is not quite functioning correctly")
                    raise Exception("A-Z sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in BlackJack Page: A=Z sorting is not disp;ayed")
            raise Exception("A-Z sorting is not functioning correctly")

    def verifycorrectSortStakesizebymaxtexttry(self, a,option):
        time.sleep(2)
        try:
            if(option==1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  #
                self.az.click()
            if (option == 2):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  #make active ascending
                self.arrow = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortarrowstakesizeasc"])
                self.arrow.click()  #
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortarrowstakesizedesc"])

            for i in range(1, a-1):  # footer images are deducted (- 5)
                print("i=",i)
                tempng1 = "Livegminmax" + str(i)
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameminmaxMap[tempng1])
                element1 = self.find_element("cssSelector", LivegameminmaxMap[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "Livegminmax" + str(i + 1)
                element2 = self.wait_for_element_visibility(10, "cssSelector", LivegameminmaxMap[tempng2])
                element2 = self.find_element("cssSelector", LivegameminmaxMap[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                sortresult = self.comparemaxparttwocurreny(text1, text2)

                if (sortresult == 1 or sortresult == 0):
                    print("Pass")
                else:
                    self.appendtofile(1,
                                      "Failure Bug in Blackjac Page: Stakesize max sorting is not quite functioning correctly")
                    raise Exception("Stakesize min sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Balcakjac Page: Stakesize max sorting is not disp;ayed")
            raise Exception("Stakesize max sorting is not functioning correctly")
    def verifycorrectSortStakesizebymintexttry(self, a,option):
        try:
            if(option==1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  #
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortstakesize"])#make active ascending arrow by clicking text
                self.arrow.click()
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortarrowstakesizeasc"])#press ascending and make descending
                self.arrow.click()  #
                self.arrow = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortarrowstakesizedesc"])#press again and make ascending
                self.arrow.click()  #

            for i in range(1, a-1):  # footer images are deducted (- 5)
                print("i=",i)
                tempng1 = "Livegminmax" + str(i)
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameminmaxMap[tempng1])
                element1 = self.find_element("cssSelector", LivegameminmaxMap[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "Livegminmax" + str(i + 1)
                element2 = self.wait_for_element_visibility(10, "cssSelector", LivegameminmaxMap[tempng2])
                element2 = self.find_element("cssSelector", LivegameminmaxMap[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                sortresult = self.compareminparttwocurreny(text1, text2)

                if (sortresult == 1 or sortresult == 0):
                    print("Pass")
                else:
                    self.appendtofile(1,
                                      "Failure Bug in Blackjac Page: Stakesize max sorting is not quite functioning correctly")
                    raise Exception("Stakesize min sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Balcakjac Page: Stakesize max sorting is not disp;ayed")
            raise Exception("Stakesize max sorting is not functioning correctly")
        #pageverificationelementexisting
    def pageverificationelementexisting(self, param):
        if (param== 1):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbyname"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page: Sort by Name A-Z text is not displayed!!")
                raise Exception("Bug Failure in Balcakjac Page:  A_Z text is not displayed!!")
        if (param== 2):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbyname"])
                element.click()
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page: Sort by Name A-Z is not changing to Z-A!!")
                raise Exception("Bug Failure in Balcakjac Page:  Z-A text is not displayed!!")
        if (param == 3):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbyname"])
                element.click()#change to Z-A
                time.sleep(1)
                element.click()  # change to A-Z
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page: Sort by Name A-Z is not changing to Z-A!!")
                raise Exception("Bug Failure in Balcakjac Page:  Z-A text is not displayed!!")
        if (param == 4):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortstakesize"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page:Stake size text is not existing!")
                raise Exception("Bug Failure in Balcakjac Page:  Page:Stake size text is not existing!")
        if (param == 5):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbytext"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbytext"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page:Stake size text is not existing!")
                raise Exception("Bug Failure in Balcakjac Page:  Page:Stake size text is not existing!")
        if (param == 6):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortnamebyarrowasc"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortnamebyarrowasc"])

            except:
                self.appendtofile(1, "Bug Failure in Balcakjac Page:Sort arrow is not existing!")
                raise Exception("Bug Failure in Balcakjac Page:  Page:Sort arrow is not existing!")



    def comparealphanumeric(self, text1, text2):

        a1 = re.split('(\d+)', text1)
        a2 = re.split('(\d+)', text2)
        print("a1[0]", str(a1[0]))
        print("a2[0]", str(a2[0]))
        print("len(a1)=", len(a1))
        # if(cmp(str(a2[0]),"Blackjack D")==0):
        #   print("Debug me")
        if (str(a1[0]) > str(a2[0])):
            return -1
        if (str(a1[0]) < str(a2[0])):
            return 1
        if (len(a1) > 1):
            if (str(a1[0] == a2[0]) and int(a1[1]) > int(a2[1])):
                return -1
        if (len(a1) > 1):
            if (str(a1[0] == a2[0]) and int(a1[1]) == int(a2[1])):
                return 0

        return 1

    def comparemaxparttwocurreny(self, a,  b):
        # if equal return 0 if the first one is higher return 1, and if the second one is higher return -1
        ta1,ta2=a.split("-")
        tb1, tb2 = b.split("-")
        ta2value = Decimal(sub(r'[^\d.]', '', ta2))
        tb2value = Decimal(sub(r'[^\d.]', '', tb2))
        if (ta2value == tb2value):
            return 0
        if (ta2value > tb2value):
            return 1
        if (ta2value< tb2value):
            return -1

    def compareminparttwocurreny(self, a, b):
        # if equal return 0 if the first one is higher return 1, and if the second one is higher return -1
        ta1, ta2 = a.split("-")
        tb1, tb2 = b.split("-")
        ta1value = Decimal(sub(r'[^\d.]', '', ta1))
        tb1value = Decimal(sub(r'[^\d.]', '', tb1))
        if (ta1value == tb1value):
            return 0
        if (ta1value > tb1value):
            return -1
        if (ta1value < tb1value):
            return 1


    def appendtofile(self, k, string):  # k= 1 is observed missing bug, k = 2 only information of tested

        d = datetime.datetime.today()
        dd = d.day

        path1 = "Bugreport_livecasino_" + str(dd) + ".txt"
        path2 = "Inforeport_livecasino_" + str(dd) + ".txt"
        # path1 = "C:\\Users\Daryoush\PycharmProjects\August24\Reports\Bugreport_livecasino_" + str(dd) + ".txt"
        # path2 = "C:\\Users\Daryoush\PycharmProjects\August24\Reports\Inforeport_livecasino_" + str(dd) + ".txt"
        if (k == 1):
            with open(path1, 'a') as wf:
                wf.write(string + "\n")
        if (k == 2):
            with open(path2, 'a') as wf:
                wf.write(string + "\n")