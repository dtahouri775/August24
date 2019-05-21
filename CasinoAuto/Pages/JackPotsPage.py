'''
Created on Septembere 06, 2018

@author: Daryoush
'''

from CasinoAuto.Locators.UIMapCasinoPage import  CasinoPageMapXpath
from CasinoAuto.Locators.UIMapJackpotsGamePage import  JackPotPageMapXpath
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Constants                                import Casino_Constants
from MatchBookLoginPage import MatchBookLoginPage
from BasePage                import BasePage
import time
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath

class JackPotsPage(BasePage):
    def __init__(self, driver):
        super(JackPotsPage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        try:
            element = self.find_element("cssSelector", CasinoPageMapXpath["AcceptCookies"])
            element.click()
        except:
            print("Bug Cookies dialog box is not there")



#defining the casino page object here
    def  _verify_page(self):
        try:

            self.jackpotsgames = self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["jackpotsLcoator"])
            self.jackpotsgames.click()

        except:
            raise Exception("jackpotsLcoator is not accessable")

    def getgamenumber(self):
        return gamenum
    def verifyAZ(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath["a_To_z"])
            self.az.click()
            element=self.find_element("cssSelector", JackPotPageMapXpath["a_To_z"])
            test1=element.text
            if(test1 == "A-Z"):
                print("Info Pass")
            else:
                raise Exception("A-Z is not active")

        except:
            raise Exception("A-Z is not displayed")

    def verifyZA(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath["a_To_z"])
            self.az.click()#make A-Z active
            self.az.click()#make Z-A active
            element = self.find_element("cssSelector", JackPotPageMapXpath["z_To_a"])
            test1 = element.text
            if (test1 == "Z-A"):
                print("Info Pass")
            else:
                raise Exception("Z-A is not active")

        except:
             raise Exception("Z-A is not displayed")
    def verifycorrectSortAZ(self):

        try:
            print("Info gamenum=",gamenum)



            self.az = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath["a_To_z"])
            self.az.click()  # make A-Z active


            for i in range(1, gamenum-6):

                tempng1 = "JackpotGamename"+str(i)
                element1 = self.find_element("cssSelector", JackPotPageMapXpath[tempng1])
                text1 = element1.get_attribute('innerText')
                print("Info text=",text1)
                tempng2 = "JackpotGamename" + str(i+1)
                element2 = self.find_element("cssSelector", JackPotPageMapXpath[tempng2])
                text2 = element2.get_attribute('innerText')
                print("Info text=", text2)
                if(text1 <= text2):
                    print("Info Pass")
                else:
                    raise Exception("A-Z sorting is not quite functioning correctly")

        except:
            raise Exception("A-Z sorting is not functioning correctly")

    def verifycorrectSortZA(self):
        try:
            self.za = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath["a_To_z"])
            self.za.click()  # make A-Z active
            self.za.click()  # make Z-A active
            print("Info gamenum=",gamenum)
            for i in range(1, gamenum - 6):
                ztempng1 = "JackpotGamename" + str(i)
                element1 = self.find_element("cssSelector", JackPotPageMapXpath[ztempng1])

                self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath[ztempng1])
                element1 = self.find_element("cssSelector",JackPotPageMapXpath[ztempng1])
                text1z = element1.get_attribute('innerText')
                print("Info text1z=",text1z)
                ztempng2 = "JackpotGamename" + str(i + 1)
                element2 = self.find_element("cssSelector", JackPotPageMapXpath[ztempng2])
                text2z = element2.get_attribute('innerText')
                if(text2z==""):
                    try:
                        element1 = self.find_element("cssSelector", "abcd")
                    except ValueBug :#Verify Game name Displays Below The Game Image
                        print("Bug The game name is not displayed")


                print("Info text2z=",text2z)
                if (text1z >= text2z):
                    print("Info Pass")


        except:
            raise Exception("A-Z sorting is not functioning correctly")

    def click_loginfromlandingpage(self, a):

        tempng1 = "JackpotsGameImage" + str(a)
        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath[tempng1])
            element1 = self.find_element("cssSelector", JackPotPageMapXpath[tempng1])
            # The game i is clicked and access to landing page
            element1.click()
        except:
            print("Bug in JackpotPage: Can not click the image! image= ",a)
        try:
            element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["LoginLandingPage1"])
            element2 = self.find_element("cssSelector", LogInPageMap["LoginLandingPage1"])
        # click on the first play for real
            element2.click()
        except:#in case it is live game
            try:
                element2 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePlaynow"])
                element2 = self.find_element("cssSelector", LiveCasinoPageMap["LivePlaynow"])
                # click on the first play for real
                element2.click()
            except:
                print("Bug in JackpotPage: Can not click the Play for real in landing page! image= ", a)

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

            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["Usernametitle"])
            element = self.find_element("cssSelector", CasinoPageMapXpath["Usernametitle"])
            text1 = element.get_attribute('innerText')
            print("Info text1=",text1)
            if (text1 == Casino_Constants["CAsino_Username"]):
                print("Info Successful Log in")
        except:
            print(" Bug Jackpot100: Either user name is not displayed or is not able to click game image to login")


    def logout(self,m):#log out and return to jackpot page
        if(m==1):
            self.jackpotgames = self.wait_for_element_visibility(10, "cssSelector",
                                                                 HomePageMapXpath["lhncasinoLocator"])
            self.jackpotgames.click()
            time.sleep(2)
            self.jackpotgames = self.wait_for_element_visibility(10, "cssSelector",
                                                                 CasinoPageMapXpath["jackpotsLcoator"])
            self.jackpotgames.click()
            time.sleep(2)

        if (m !=1):
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["logout"])
            element2 = self.find_element("cssSelector", HomePageMapXpath["logout"])
            element2.click()
            time.sleep(2)
            self.jackpotgames = self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhncasinoLocator"])
            self.jackpotgames.click()
            time.sleep(2)
            self.jackpotgames = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["jackpotsLcoator"])
            self.jackpotgames.click()
            time.sleep(2)
    #verifyj ackpotamount is displayed
    def verifyjackpotamountlandingpage(self,a):
        jamountimage=0
        jamountlanding=0

        tempng2 = "JackpotsGameImage" + str(a)
        tempng1="JackpotAmount" + str(a)

        try:
            element1 = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath[tempng2])
            element1 = self.find_element("cssSelector", JackPotPageMapXpath[tempng2])
            element2 = self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath[tempng1])
            element2 = self.find_element("cssSelector", JackPotPageMapXpath[tempng1])
            stringvalue=element2.text
            print("Info stringvalue=",stringvalue)
            jamountimage = float(stringvalue[-6:])
            print("Info end 5 digit of jamountimage=",jamountimage )
             # The game i is clicked and access to landing page
            element1.click()
        except:
            print("Bug in JackpotPage: Can not click the image! image= ", a)

        try:
            self.wait_for_element_visibility(10, "cssSelector", JackPotPageMapXpath["Jackpotamtlandingpage"])
            element1 = self.find_element("cssSelector",JackPotPageMapXpath["Jackpotamtlandingpage"])
            stlpjpvalue = element1.text
            jamountlanding = float(stlpjpvalue[-6:])
            print("Info end 5 digit ofjamountlandingpage=", jamountlanding)

        except:
            print("Bug in JackpotPage: Can not display jackpot amount! image= ", a)

        differenceValue =  abs(jamountimage - jamountlanding)
        print("Info differenceValue=",differenceValue)
        if(differenceValue<5):
            print("Info Jackpot difference displayed on landing page and image file are less than 5")
        else:
            raise Exception("Bug: Jackpot difference displayed on landing page and image file are more than 5")


