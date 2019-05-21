'''
Created on December 11, 2018
Changed on December 20
@author: Daryoush
Moddified on December 22
Change on January 24, 2019
'''
from BasePage import BasePage
from CasinoAuto.Constants                                import Casino_Constants
import time
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegamenameMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameDealernameMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameminmaxMap
from CasinoAuto.Locators.UIMapLiveCasino import LiveInfoPageMap
from CasinoAuto.Locators.UIMapLiveCasino import LivegameImagePageMap

from CasinoAuto.Locators.UIMapLiveCasino import LiveroulettePageMap
from CasinoAuto.Locators.UIMapLiveCasino import LiveGameRoulettePastResults
from CasinoAuto.Locators.UIMapLiveCasino import LiveGameRouletteLandingPageResults
from MatchBookLoginPage import MatchBookLoginPage
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath
from CasinoAuto.Locators.UIMapCasinoPage import CasinoPageMapXpath
from CasinoAuto.Locators.UIMapLiveCasino import LiveProviderLogNameMap
from CasinoAuto.Locators.UIMapLiveCasino import Livegamescommon
import datetime
import re
from re import sub
from decimal import Decimal
class LiveroulettePage(BasePage):
    def __init__(self, driver):
        super(LiveroulettePage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        #webElementsList = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[4]/div/div[4]/div/')
        global gamenum
        gamenum = len(webElementsList)
        print(gamenum)
        global deductedimage
        #The deducted number for some pages are different
        deductedimage = gamenum - 16  # 5 may be modified based on modification on this page
    # defining the casino page object here
        try:
            element = self.find_element("cssSelector", LiveCasinoPageMap["AcceptCookies"])
            element.click()
        except:
            print("Cookies dialog box is not there")

    def _verify_page(self):
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()


            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveRoulette"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveRoulette"])
            element1.click()

        except:
            raise Exception("LiveRoulette locator or livecasinoLocatortop is not accessable")

    def liveroulette(self):
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveRoulette"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveRoulette"])
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
                text1 = element.get_attribute('innerText')
                #text1 = element.text
                print(text1)

                if (text1 !=""):
                    print("Successful Log in")
                element = self.find_element("cssSelector", CasinoPageMapXpath["rhsaccount"])#close rhsa
                element.click()
            except:
                raise Exception(" user name is not displayed")
            tempng1 = "LiveGameimage" + str(a)
            try:  # click game image again after logged in to load the game
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameImagePageMap[tempng1])
                element1 = self.find_element("cssSelector", LivegameImagePageMap[tempng1])
                try:
                    element1.click()
                    return 1
                except:
                    print("Bug Live Roulette Page:Element Livegamelaunch is not clickable yet, probably image is not there! Element=",a)
                    self.appendtofile(1, "Bug Live Roulette Page:Element Livegamelaunch is not clickable yet, probably image is not there! game=" + str(a))
                    return 0
            except:
                print(
                "Bug Live Roulette Page:Element  image in Roulette page is not clickable yet, probably image is not there! Element=",
                a)
                self.appendtofile(1,
                                  "Bug Live Roulette Page:Element  image in Roulette page is not clickable yet, probably image is not there! Element=" + str(
                                      a))
            tempng1 = "LiveGameimage" + str(a)
            try:  # click game image again after logged in to load the game
                element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameImagePageMap[tempng1])
                element1 = self.find_element("cssSelector", LivegameImagePageMap[tempng1])
                try:
                    element1.click()
                    return 1
                except:
                    print(
                    "Bug Live Roulette Page:Element Livegamelaunch is not clickable yet, probably image is not there! Element=",
                    a)
                    self.appendtofile(1,"Bug Live Roulette Page:Element Livegamelaunch is not clickable yet, probably image is not there! game=" + str(a))
                    return 0
            except:
                print(
                "Bug Live Roulette Page:Element  image in Roulette is not available yet, probably image is not there! Element=",
                a)
                self.appendtofile(1,
                                  "Bug Live Roulette Page:Element Livegamelaunch is not available yet, probably image is not there! game=" + str(
                                      a))

            return (text1)

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
            try:
                element3 = self.find_element("cssSelector", HomePageMapXpath["MBNothank"])
                element3.click()
            except:
                print(" ")
                #print("No thanks dialog box is not displayed which is ok")
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveRoulette"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveRoulette"])
            element1.click()

            try:
                element3 = self.find_element("cssSelector", HomePageMapXpath["MBNothank"])
                element3.click()
            except:
                print(" ")
                #print("No thanks dialog box is not displayed which is ok")

    def verifylandingpageinfo(self,a):
        er=0
        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveInfoPageMap[tempng1])
        element1 = self.find_element("cssSelector", LiveInfoPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:

            element1.click()
        except:
            print("Not able to click  <i> button, may be covered by bet slip Bug  200i: element->",a)
            self.appendtofile(1,"Bug Live Roulette page:Not able to click  <i> button, : element->" + str(a))
            er=1

        if(er==0):#if accessed to landing page

            #verify game name
            try:
                gamename = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgname"])
                gamename = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgname"])
                text = gamename.text
                #print(text)
            except:
                self.appendtofile(1, "Bug Live Roulette: Game Name is not available Bug Note: This is failure bug, : element->" + str(a))
                raise Exception("Game Name is not available Bug ")
            #print("Game name is: ",text)
            #verify game provider
            try:
                gameprovider = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPprovider"])
                gameprovider = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPprovider"])

            except:
                self.appendtofile(1, "Bug Live Roulette: Game Provider is not available! Note: This is failure bug, : element->" + str(a))
                raise Exception("Game Provider is not available!")


            #verify game rule is there
            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgamerule"])
                gamerule = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgamerule"])

            except:
                self.appendtofile(1,
                                  "Bug Live Roulette:  Game Rule is not available! Note: This is failure bug, : element->" + str(a))
                raise Exception("Game Rule is not available Bug :201")

                # verify game description is there
            try:
                gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                text = gamedes.text
                #print("Game description is:",text)
            except:
                self.appendtofile(1,
                                  "Bug Live Roulette: Game Descritpin is not available!!, : element->" + str(a))
                print("Bug Game Descritpin is not available Bug :201 gamenumber=",a)

            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePlaynow"])
                gamerule = self.find_element("cssSelector", LiveCasinoPageMap["LivePlaynow"])
                #print("Live Play now is displayed")
            except:
                self.appendtofile(1,
                                  "Bug Live Roulette: LivePlaynow is not available ! Note: This is failure bug, : element->" + str(a))
                raise Exception("LivePlaynow is not available Bug :202")

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
                print("element is not clickable yet, probably image is not there!")
                return 0

        except:
            return 0
    def verifyproviderlog(self,a):
        tempng1 = "ProviderLog" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap[tempng1])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap[tempng1])
            try:
                #print("Assumption is all the images are there")
                return element1.get_attribute(('id'))
            except:
                print("ProviderLog is not there!")
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
            try:#clicking game name opens login dialog box which is not purpose of this test
                #print("Assumption is all the images are there")
                return 1
            except:
                print("ProviderLog is not there!")
                return 0

        except:
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
            self.appendtofile(1,"Bug Live Roulette: Provider min-max is not there!  Elment="+str(a))
            print("Provider min-max is not there! Bug Live100 A=",a)
            return 0
    def verifyavailablenumbers(self,a):
        historymainpage = []
        for x in range(1, 6):
            tempng1 = "Livegameresult" + str(a)+"_"+str(x) #verify first number is there, may expand up to five number in future based on need
            try:
                element1 = self.wait_for_element_visibility(10, "cssSelector", LiveGameRoulettePastResults[tempng1])
                element1 = self.find_element("cssSelector", LiveGameRoulettePastResults[tempng1])
                displayednumber = element1.text
                historymainpage.append(displayednumber)
                #print("Info Ok, availability of recent game result of Roulette game: ",displayednumber)
                #return 1;
            except:
                self.appendtofile(1, "Bug  Live Roulette: for Not availability recent game result of Roulette game: Element= " + str(a))
                print("Bug  for Not availability recent game result of Roulette game: Element= ",a)
                return -1
        return historymainpage
        return 1
    def verifyavailablenumberslandingpage(self,a):

        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveInfoPageMap[tempng1])
        element1 = self.find_element("cssSelector", LiveInfoPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:
            element1.click()
            time.sleep(1)
        except:
            self.appendtofile(1, "Bug Live Roulette: Not able to click  <i> button, : element-> " + str(a))
            print("Not able to click  <i> button, may be covered by bet slip Bug  200i: element->", a)

        historylandingpage = []
        for x in range(1, 6):
            tempng1 = "Livegamelandigresult"+str(x) #verify first number is there, may expand up to five number in future based on need
            try:
                element1 = self.wait_for_element_visibility(10, "cssSelector", LiveGameRouletteLandingPageResults[tempng1])
                element1 = self.find_element("cssSelector", LiveGameRouletteLandingPageResults[tempng1])
                displayednumber = element1.text
                historylandingpage.append(displayednumber)
                #print("Info Ok, availability of recent game result of landing page Roulette game: ",displayednumber)
                #return 1;
            except:
                self.appendtofile(1, "Bug Live Roulette:  Livegamelandigresult, : element-> " + str(x))
                #print("numbers in main page and landing pager are matching game_num= Element= ",x)
                element2 = self.find_element("cssSelector",Livegamescommon["Livebreadcrumbl"])  # return to main page of roulette
                element2.click()
                time.sleep(1)
                return -1
        element2 = self.find_element("cssSelector", Livegamescommon["Livebreadcrumbl"])#return to main page of roulette
        element2.click()
        time.sleep(1)
        return historylandingpage
    #
    def navaigatetofeaturepage(self):
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveLobby"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveLobby"])
            element1.click()
            return 1
        except:
            self.appendtofile(1, "Bug Live Roulette:  Can not navaigate to featurepage!!")
            print("Can not navaigate to featurepage")
            return 0

    def verifydealername(self,a):
        tempng1 = "LiveDealername" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivegameDealernameMap[tempng1])
            element1 = self.find_element("cssSelector", LivegameDealernameMap[tempng1])
            return 1;
        except:
            self.appendtofile(1, "Bug Live Roulette:  Dealer name is not there! (Make sure it it not auto Roulette): element-> " + str(a))
            print("Dealer name is not there! Bug Live101 A=",a)
            return 0

    def verifycorrectSortZA(self, a, option):
        try:
            if (option == 1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                self.az.click()  # make A-Z active
            # Livesortnamebyarrowdesc
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortnamebyarrowasc"])
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
                                      "Faiure Bug in Roulette Page: Z-A sorting is not quite functioning correctly")
                    raise Exception("A-Z sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Roulette Page: Z-A sorting is not displayed for clicking")
            raise Exception("Z-A sorting is not  displayed for clicking")

    def verifycorrectSortAZ(self, a, option):
        try:
            if (option == 1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortnamebyarrowasc"])
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
                sortresult = self.comparealphanumeric(text1, text2)
                if (cmp(text1, text2) == 0):
                    sortresult = 0
                if (sortresult == 1 or sortresult == 0):
                    print("Pass")
                else:
                    self.appendtofile(1,
                                      "Failure Bug in Roulette Page: A-Z sorting is not quite functioning correctly")
                    raise Exception("A-Z sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Roulette Page: A=Z sorting is not disp;ayed")
            raise Exception("A-Z sorting is not functioning correctly")

    def verifycorrectSortStakesizebymaxtexttry(self, a, option):
        time.sleep(2)
        try:
            if (option == 1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  #
                self.az.click()
            if (option == 2):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  # make active ascending
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortarrowstakesizeasc"])
                self.arrow.click()  #
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon["Livesortarrowstakesizedesc"])

            for i in range(1, a - 1):  # footer images are deducted (- 5)
                print("i=", i)
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
                                      "Failure Bug in Roulette Page: Stakesize max sorting is not quite functioning correctly")
                    raise Exception("Stakesize min sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Roulette Page: Stakesize max sorting is not disp;ayed")
            raise Exception("Stakesize max sorting is not functioning correctly")

    def verifycorrectSortStakesizebymintexttry(self, a, option):
        try:
            if (option == 1):
                self.az = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                self.az.click()  #
            if (option == 2):
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon[
                                                                  "Livesortstakesize"])  # make active ascending arrow by clicking text
                self.arrow.click()
                self.arrow = self.wait_for_element_visibility(10, "cssSelector",
                                                              Livegamescommon[
                                                                  "Livesortarrowstakesizeasc"])  # press ascending and make descending
                self.arrow.click()  #
                self.arrow = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon[
                    "Livesortarrowstakesizedesc"])  # press again and make ascending
                self.arrow.click()  #

            for i in range(1, a - 1):  # footer images are deducted (- 5)
                print("i=", i)
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
                                      "Failure Bug in Roulette Page: Stakesize max sorting is not quite functioning correctly")
                    raise Exception("Stakesize min sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Bug Failure in Roulette Page: Stakesize max sorting is not disp;ayed")
            raise Exception("Stakesize max sorting is not functioning correctly")

    def pageverificationelementexisting(self, param):
        if (param== 1):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbyname"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Roulette Page: Sort by Name A-Z text is not displayed!!")
                raise Exception("Bug Failure in Roulette Page:  A_Z text is not displayed!!")
        if (param== 2):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbyname"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbyname"])
                element.click()
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Roulette Page: Sort by Name A-Z is not changing to Z-A!!")
                raise Exception("Bug Failure in Roulette Page:  Z-A text is not displayed!!")
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
                self.appendtofile(1, "Bug Failure in Roulette Page: Sort by Name A-Z is not changing to Z-A!!")
                raise Exception("Bug Failure in Roulette Page:  Z-A text is not displayed!!")
        if (param == 4):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortstakesize"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortstakesize"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Roulette Page:Stake size text is not existing!")
                raise Exception("Bug Failure in Roulette Page:  Page:Stake size text is not existing!")
        if (param == 5):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortbytext"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortbytext"])
                name = element.get_attribute('innerText')
                return name
            except:
                self.appendtofile(1, "Bug Failure in Roulette Page:Stake size text is not existing!")
                raise Exception("Bug Failure in Roulette Page:  Page:Stake size text is not existing!")
        if (param == 6):
            try:
                element = self.wait_for_element_visibility(10, "cssSelector", Livegamescommon["Livesortnamebyarrowasc"])
                element = self.find_element("cssSelector", Livegamescommon["Livesortnamebyarrowasc"])

            except:
                self.appendtofile(1, "Bug Failure in Roulette Page:Sort arrow is not existing!")
                raise Exception("Bug Failure in Roulette Page:  Page:Sort arrow is not existing!")
    def comparealphanumeric(self, text1, text2):

        a1 = re.split('(\d+)', text1)
        a2 = re.split('(\d+)', text2)
        print("a1[0]", str(a1[0]))
        print("a2[0]", str(a2[0]))
        print("len(a1)=", len(a1))

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
    def nothanks(self):
        try:
            element3 = self.find_element("cssSelector", HomePageMapXpath["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"
    def Diff(self,li1, li2):
        return (list(set(li1) - set(li2)))

    def appendtofile(self, k, string):# k= 1 is observed missing bug, k = 2 only information of tested
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