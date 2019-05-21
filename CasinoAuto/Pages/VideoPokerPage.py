
'''
Created on October 12, 2018

@author: Daryoush
Moddified on September 14
Modified on Feb 04 2019 to implement new logic in Play for Fun
'''

from CasinoAuto.Locators.UIMapCasinoPage import CasinoPageMapXpath
from CasinoAuto.Locators.UIMapVideoPokerGamesPage import VideoPokerGamePageMapXpath
from CasinoAuto.Locators.UIMapVideoPokerGamesPage import VideoPokerGamePageMaptype
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Constants                import Casino_Constants
from MatchBookLoginPage import MatchBookLoginPage
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath

# from BasePage                import IncorrectPageException

from BasePage import BasePage
import time
import datetime

class VideoPokerPage(BasePage):
    def __init__(self, driver):
        super(VideoPokerPage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        print(gamenum)
    # defining the casino page object here
        try:
            element = self.find_element("cssSelector", CasinoPageMapXpath["AcceptCookies"])
            element.click()
        except:
            print("Cookies dialog box is not there")


    def _verify_page(self):
        try:

            self.vpgames = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["videopokerlocator"])
            self.vpgames.click()

        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Video Poker Locator is not available! ")
            raise Exception("videopokerlocatorXpath is not accessable")


    def getgamenumber(self):
        return gamenum

    def verifyAZ(self):
        try:
            time.sleep(2)
            self.az = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath["a_To_z"])
            self.az.click()
            element = self.find_element("cssSelector", VideoPokerGamePageMapXpath["a_To_z"])
            test1 = element.text
            if (test1 == "A-Z"):
                print("Pass")
            else:
                self.appendtofile(1, "Failure bug Video Poker Page: A_Z is not active! ")
                raise Exception("A-Z is not active")

        except:
            self.appendtofile(1, "Failure bug Video Poker Page: A-Z is not displayed! ")
            raise Exception("A-Z is not displayed")

    def verifyZA(self):
        try:
            time.sleep(2)
            self.az = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath["a_To_z"])
            self.az.click()  # make A-Z active
            self.az.click()  # make Z-A active
            element = self.find_element("cssSelector", VideoPokerGamePageMapXpath["z_To_a"])
            test1 = element.text
            if (test1 == "Z-A"):
                print("Pass")
            else:
                self.appendtofile(1, "Failure bug Video Poker Page: Z-A is not active! ")
                raise Exception("Z-A is not active")

        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Z-A is not displayed!! ")
            raise Exception("Z-A is not displayed")

    def verifycorrectSortAZ(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath["a_To_z"])
            self.az.click()  # make A-Z active
            for i in range(1, gamenum-6):# footer images are deducted (- 5)

                tempng1 = "VideoPokerGamename"+str(i)
                element1 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "VideoPokerGamename"+str(i+1)
                element2 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                if (text2 == ""):
                    try:
                        element1 = self.find_element("cssSelector", "abcd")
                    except :  # Verify Game name Displays Below The Game Image
                        print("The game name is not displayed")

                if(text1 <= text2):
                    print("Pass")
                else:
                    self.appendtofile(1, "Failure bug Video Poker Page: A-Z soring is not functioning correctly! ")
                    raise Exception("A-Z sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Z-A is not displayed!!! ")
            raise Exception("A-Z sorting is not displayed")

    def verifycorrectSortZA(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath["a_To_z"])
            self.az.click()  # make A-Z active
            self.az.click()  # make Z-A active

            for i in range(1, gamenum-6):# footer images are deducted (- 5)

                tempng1 = "VideoPokerGamename"+str(i)
                element1 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "VideoPokerGamename"+str(i+1)
                element2 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                if(text1 >= text2):
                    print("Pass")
                else:
                    self.appendtofile(1, "Failure bug Video Poker Page: Z-A is not functioning correctly! ")
                    raise Exception("Z-A sorting is not quite functioning correctly")
        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Z-A is not displayed!! ")
            raise Exception("Z-A sorting is not functioning correctly")
    def click_loginfromlandingpage(self, a):

            tempng1 = "VideoPokerGameImage" + str(a)
            element1 = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath[tempng1])
            element1 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng1])
            # The game i is clicked and access to landing page
            element1.click()
            time.sleep(2)
            element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["LoginLandingPage1"])
            element1 = self.find_element("cssSelector", LogInPageMap["LoginLandingPage1"])
            # click on the first play for real
            element2.click()
            time.sleep(1)
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
                self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["rhsaccount"])
                element = self.find_element("cssSelector", HomePageMapXpath["rhsaccount"])
                element.click()
                time.sleep(2)
                self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["Usernametitle"])
                element = self.find_element("cssSelector", CasinoPageMapXpath["Usernametitle"])
                text1 = element.get_attribute('innerText')
                print(text1)
                if (text1 == Casino_Constants["CAsino_Username"]):
                    print("Successful Log in")



            except:
                self.appendtofile(1, "Failure bug Video Poker Page: user name is not displayed! ")
                raise Exception(" user name is not displayed")
            return (text1)

    def logout(self):



        self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["logout"])
        element2 = self.find_element("cssSelector", CasinoPageMapXpath["logout"])
        element2.click()
        time.sleep(2)
        self.click(10, "cssSelector", HomePageMapXpath["topcasinoLocator"])
        time.sleep(2)
        self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["videopokerlocator"])
        element2 = self.find_element("cssSelector", CasinoPageMapXpath["videopokerlocator"])
        element2.click()
        time.sleep(2)

        # only for zero balnce user may be needed.

        try:
            element3 = self.find_element("cssSelector", HomePageMapXpath["Nothanksbutton"])
            element3.click()
        except:
            print "No thanks dialog box is not displayed which is ok"




    def click_playforfunfromlandingpagevpokergames(self, a, z):

        tempng1 = "VideoPokerGameImage" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath[tempng1])
        element1 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng1])
        # The game i is clicked and access to landing page
        element1.click()
        time.sleep(2)
        buttonname = "None"
        try:
            element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["PlayforFun"])
            element2 = self.find_element("cssSelector", LogInPageMap["PlayforFun"])
            buttonname = element2.text
            if (buttonname != 'PLAY FOR FUN'):
                try:
                    element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["PlayforFun"])
                    element2 = self.find_element("cssSelector", LogInPageMap["PlayforFun"])
                    buttonname = element2.text
                except:
                    print("Check to make sure it is live Dealer game that do not have play for fun button!")
        except:
            print("Check to make sure it is live Dealer game that do not have play for fun button!")

        print(buttonname)
        if (buttonname == 'PLAY FOR FUN'):
            element2.click()
            time.sleep(1)
            if (z == 0):
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
                # print("testpoint4")
                log_obj.login()
                time.sleep(5)



        else:
            print"This game do not have play for fun check to make sure it is live game!"
        testedurl = self.driver.current_url
        element2 = self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2 = self.find_element("cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2.click()
        time.sleep(3)
        element2.click()  # just to make sure

        try:
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["rhsaccount"])
            element = self.find_element("cssSelector", HomePageMapXpath["rhsaccount"])
            element.click()
            time.sleep(2)
        except:
            print("Info: rhsaccount is not displayed!")
        return (testedurl)
    def verifylandingpageinfo(self,a):
        tempng1 = "VideoPokerGameImage" + str(a)
        element1 = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMapXpath[tempng1])
        element1 = self.find_element("cssSelector", VideoPokerGamePageMapXpath[tempng1])
        # The game i is clicked and access to landing page
        element1.click()
        # verify landing page game information
        #verify game name
        try:
            gamename = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgname"])
            gamename = self.find_element("cssSelector", CasinoPageMapXpath["LPgname"])
            text = gamename.text
            print(text)
        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Game name is not displayed! ")
            raise Exception("Game Name is not available Bug :200")
        print("Game name is: ",text)
        #verify game provider
        try:
            gameprovider = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPprovider"])
            gameprovider = self.find_element("cssSelector", CasinoPageMapXpath["LPprovider"])

        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Game Provider is not displayed! ")
            raise Exception("Game Provider is not available Bug :201")

        #verify game rule is there
        try:
            gamerule = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamerule"])
            gamerule = self.find_element("cssSelector", CasinoPageMapXpath["LPgamerule"])

        except:
            self.appendtofile(1, "Failure bug Video Poker Page: Game Rule is not there! ")
            raise Exception("Game Rule is not available Bug :201")

            # verify game description is there
        try:
            gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
            gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
            text = gamedes.text
            print("Game description is:",text)
        except:
            try:
                gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionmatchbook"])
                gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionmatchbook"])
                text = gamedes.text
                print("Game description is:", text)
            except:
                try:
                    gamedes = self.wait_for_element_visibility(10, "cssSelector",
                                                               CasinoPageMapXpath["LPgamedescriptionnetent"])
                    gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionnetent"])
                    text = gamedes.text
                    print("Game description is:", text)
                except:
                    self.appendtofile(1, "Failure bug Video Poker Page:Game descritpin is not available! ")
                    raise Exception("Bug Game Descritpin is not available Bug :201")

        element1 = self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2 = self.find_element("cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2.click()
        time.sleep(1)
        element2.click()  # just to make sure
        self.click(10,
                   "cssSelector",
                   CasinoPageMapXpath["videopokerlocator"]
                   )
    def veifygametype(self, a):

            tempng1 = "Vgtype" + str(a)
            element1 = self.wait_for_element_visibility(10, "cssSelector", VideoPokerGamePageMaptype[tempng1])
            element1 = self.find_element("cssSelector", VideoPokerGamePageMaptype[tempng1])
            # The game i is clicked and access to landing page
            element1.click()
            temp = element1.text
            if(temp=="VIDEO POKER"):#TOMORROW CONTINUE FROM HERE
                print("Pass")
            else:
                try:
                    element1 = self.wait_for_element_visibility(10, "cssSelector", "Slots is not written under slots game")
                except  :
                    print("Table Games is not written under slots game")

            return(temp)

    def nothanks(self):
        try:
            element3 = self.find_element("cssSelector", HomePageMapXpath["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"

    def appendtofile(self, k, string):  # k= 1 is observed missing bug, k = 2 only information of tested
        d = datetime.datetime.today()
        dd = d.day

        path1 = "Bugreport_classiccasino_" + str(dd) + ".txt"
        path2 = "Inforeport_classiccasino_" + str(dd) + ".txt"
        # path1 = "C:\\Users\Daryoush\PycharmProjects\August24\Reports\Bugreport_classiccasino_" + str(dd) + ".txt"
        # path2 = "C:\\Users\Daryoush\PycharmProjects\August24\Reports\Inforeport_classiccasino_" + str(dd) + ".txt"
        if (k == 1):
            with open(path1, 'a') as wf:
                wf.write(string + "\n")
        if (k == 2):
            with open(path2, 'a') as wf:
                wf.write(string + "\n")