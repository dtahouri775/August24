'''
Created on December 11, 2018
Changed on December 20
@author: Daryoush
Moddified on December 22
'''
from BasePage import BasePage
from CasinoAuto.Constants                                import Casino_Constants
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
import time
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
from CasinoAuto.Locators.UIMapLiveCasino import LivepokerPageMap
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from MatchBookLoginPage import MatchBookLoginPage
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath
from CasinoAuto.Locators.UIMapCasinoPage import CasinoPageMapXpath

class LivepokerPage(BasePage):
    def __init__(self, driver):
        super(LivepokerPage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        print("Info gamenum=",gamenum)
    # defining the casino page object here
        try:
            element = self.find_element("cssSelector", LiveCasinoPageMap["AcceptCookies"])
            element.click()
        except:
            print("Bug in Poker Page:Cookies dialog box is not there")

    def _verify_page(self):
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()


            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePoker"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LivePoker"])
            element1.click()

        except:
            raise Exception("Live Pokerlocator or livecasinoLocatortop is not accessable")

    def livepoker(self):
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePoker"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LivePoker"])
        element1.click()

    def getgamenumber(self):
        return gamenum

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
                self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["usernametitle"])
                element = self.find_element("cssSelector", CasinoPageMapXpath["usernametitle"])

                text1 = element.get_attribute('innerText')
                #text1 = element.text
                print("Info element=",text1)

                if (text1 !=""):
                    print("Info Successful Log in")

            except:
                raise Exception(" user name is not displayed")

            return (text1)

    def logout(self):



            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["topcasinoLocator"])
            element3 = self.find_element("cssSelector", HomePageMapXpath["topcasinoLocator"])
            time.sleep(2)
            element3.click()
            # self.click(10,"xpath",HomePageMapXpath["lhncasinoLocatorXpath"])

            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["usernametitle"])

            element = self.find_element("cssSelector", CasinoPageMapXpath["usernametitle"])
            element.click()

            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["logout"])
            element2 = self.find_element("cssSelector", CasinoPageMapXpath["logout"])
            element2.click()
            time.sleep(5)
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            element1.click()
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePoker"])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap["LivePoker"])
            element1.click()

         #only for zero balnce user may be needed.

            try:
                element3 = self.find_element("cssSelector", HomePageMapXpath["MBNothank"])
                element3.click()
            except:
                print "Bug in Poker Page:No thanks dialog box is not displayed which is ok"

    def verifylandingpageinfo(self,a):
        er=0
        tempng1 = "Liveinfo" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", LivepokerPageMap[tempng1])
        element1 = self.find_element("cssSelector", LivepokerPageMap[tempng1])
        # The game i is clicked and access to landing page
        try:

            element1.click()
        except:
            print("Bug in Poker Page:Not able to click  <i> button, may be covered by bet slip Error 200i: element->",a)
            er=1

        if(er==0):#if accessed to landing page

            #verify game name
            try:
                gamename = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgname"])
                gamename = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgname"])
                text = gamename.text
                print("Info gamename= ",text)
            except:
                print("Bug Game Name is not available Error:200 element=",a)#raise Exception
            print("Info Game name is: ",text)
            #verify game provider
            try:
                gameprovider = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPprovider"])
                gameprovider = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPprovider"])

            except:
                raise Exception("Game Provider is not available Error:201")

            #verify game rule is there
            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LiveLPgamerule"])
                gamerule = self.find_element("cssSelector", CasinoPageMapXpath["LiveLPgamerule"])

            except:
                raise Exception("Game Rule is not available Error:201")

                # verify game description is there
            try:
                gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
                text = gamedes.text
                print("Info Game description is:",text)
            except:
                print("Bug Live Poker Page:Element Game Descritpin is not available Elment=",a)
                #raise Exception("Game Descritpin is not available Error:201")# we may use this based on Sam feed back.
                #putting this statement will not let to continue testing other games,
            try:
                gamerule = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePlaynow"])
                gamerule = self.find_element("cssSelector", LiveCasinoPageMap["LivePlaynow"])
                print("Info Live Play now is displayed")
            except:
                raise Exception("LivePlaynow is not available Error:202")

            #LivePlaynow
            element2 = self.find_element("cssSelector", LivepokerPageMap["landingpoker"])
            element2.click()
            time.sleep(1)


    def existgameimage(self,a):
        tempng1 = "LivePokerGameimage" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivepokerPageMap[tempng1])
            element1 = self.find_element("cssSelector", LivepokerPageMap[tempng1])
            try:
                element1.click()
                return 1
            except:
                print("Bug Live Poker Page:element is not clickable yet, probably image is not there! element=",a)
                return 0

        except:
            return 0
    def verifyproviderlog(self,a):
        tempng1 = "ProviderLog" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap[tempng1])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap[tempng1])
            try:
                print("Ino Assumption is all the images are there")
                return 1
            except:
                print("Bug Live Poker Page:ProviderLog is not there! element=",a)
                return 0

        except:
            return 0

    # live game name under images
    def verifygamename(self,a):
        tempng1 = "Livegname" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LivepokerPageMap[tempng1])
            element1 = self.find_element("cssSelector", LivepokerPageMap[tempng1])
            try:#clicking game name opens login dialog box which is not purpose of this test
                print("Info Assumption is all the images are there")
                return 1
            except:
                print("Bug Live Poker Page:ProviderLog is not there!")
                return 0

        except:
            return 0

    #verifygame min-max existing next to info icon

    def verifygameminmax(self,a):
        tempng1 = "Livegminmax" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap[tempng1])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap[tempng1])
            return 1;
        except:
            print("Bug Live Poker Page:Provider min-max is not there! ErrorLive100 A=",a)
            return 0
    def verifydealername(self,a):
        tempng1 = "LiveDealername" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap[tempng1])
            element1 = self.find_element("cssSelector", LiveCasinoPageMap[tempng1])
            return 1;
        except:
            print("Bug Live Poker Page:Dealer name is not there! ErrorLive101 A=",a)
            return 0