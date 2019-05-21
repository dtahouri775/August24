'''
Created on Septembere 06, 2018

@author: Daryoush
'''

from CasinoAuto.Locators.UIMapCasinoPage import  CasinoPageMapXpath
from CasinoAuto.Locators.UIMapNewGamesPage import  NewPageMapXpath
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Constants                                import Casino_Constants
from MatchBookLoginPage import MatchBookLoginPage
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath
from BasePage                import BasePage
import time
import datetime

class NewGamesPage(BasePage):
    def __init__(self, driver):
        super(NewGamesPage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        print(gamenum)
        try:
            element = self.find_element("cssSelector", CasinoPageMapXpath["AcceptCookies"])
            element.click()
        except:
            print("Cookies dialog box is not there")



        #defining the casino page object here
    def  _verify_page(self):
        try:

            self.newgames = self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["newgameLocator"])
            self.newgames.click()

        except:
            self.appendtofile(1, "Bug Failure: newgameLocator is not accessable")
            raise Exception("newgameLocator is not accessable")

    def getgamenumber(self):
        return gamenum

    def verifyAZ(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath["a_To_z"])
            self.az.click()
            element=self.find_element("cssSelector", NewPageMapXpath["a_To_z"])
            test1=element.text
            if(test1 == "A-Z"):
                self.appendtofile(2,"Passing A-Z")
                print("Pass")
            else:
                self.appendtofile(1, "Bug : A-Z is not active")
                raise Exception("A-Z is not active")

        except:
            self.appendtofile(1, "Bug Failure: A-Z is not displayed")
            raise Exception("A-Z is not displayed")

    def verifyZA(self):
        try:
            self.az = self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath["a_To_z"])
            self.az.click()#make A-Z active
            self.az.click()#make Z-A active
            element = self.find_element("cssSelector", NewPageMapXpath["z_To_a"])
            test1 = element.text
            if (test1 == "Z-A"):
                self.appendtofile(2, "Info New Game page Passing Z-A")
                print("Pass")
            else:
                self.appendtofile(1, "Bug : Z-A is not active")
                raise Exception("Z-A is not active")

        except:
            self.appendtofile(1, "Bug Failure: Z-A is not displayed")
            raise Exception("Z-A is not displayed")
    def verifycorrectSortAZ(self):

        try:

            print(gamenum)



            self.az = self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath["a_To_z"])
            self.az.click()  # make A-Z active


            for i in range(1, gamenum-6):# footer images are deducted (- 6)
                print("i=",i)
                tempng1 = "NewGamename"+str(i)
                element1 = self.find_element("cssSelector", NewPageMapXpath[tempng1])
                text1 = element1.get_attribute('innerText')
                print(text1)
                tempng2 = "NewGamename" + str(i+1)
                element2 = self.find_element("cssSelector", NewPageMapXpath[tempng2])
                text2 = element2.get_attribute('innerText')
                print(text2)
                if(text1 <= text2):
                    print("Pass")
                else:
                    self.appendtofile(1, "Bug Failure Newgame Page: A-Z sorting is not functioning correctly")
                    raise Exception("A-Z sorting is not quite functioning correctly")

        except:
            self.appendtofile(1, "Bug Failure: Newgame Page:A-Z sorting is not functioning correctly!!")
            raise Exception("A-Z sorting is not functioning correctly")

    def verifycorrectSortZA(self):
        try:
            self.za = self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath["a_To_z"])
            self.za.click()  # make A-Z active
            self.za.click()  # make Z-A active
            print(gamenum)
            for i in range(1, gamenum - 6):
                ztempng1 = "NewGamename" + str(i)
                element1 = self.find_element("cssSelector", NewPageMapXpath[ztempng1])

                self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath[ztempng1])
                element1 = self.find_element("cssSelector",NewPageMapXpath[ztempng1])
                text1z = element1.get_attribute('innerText')
                print(text1z)
                ztempng2 = "NewGamename" + str(i + 1)
                element2 = self.find_element("cssSelector", NewPageMapXpath[ztempng2])
                text2z = element2.get_attribute('innerText')
                print(text2z)
                if (text2z == ""):
                    try:
                        element1 = self.find_element("cssSelector", "abcd")
                    except :  # Verify Game name Displays Below The Game Image
                        self.appendtofile(1, "Bug Newgame page: The game name is not displayed")
                        print("The game name is not displayed")

                if (text1z >= text2z):
                    print("Pass")


        except:
            self.appendtofile(1, "Bug Failure: Newgame Page:A-Z sorting is not functioning correctly!")
            raise Exception("A-Z sorting is not functioning correctly")

    def click_loginfromlandingpage(self,a):


            tempng1 = "NewGameImage" + str(a)
            element1 = self.wait_for_element_visibility(10, "cssSelector", NewPageMapXpath[tempng1])
            element1 = self.find_element("cssSelector", NewPageMapXpath[tempng1])
            #The game i is clicked and access to landing page
            element1.click()
            try:
                element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["LoginLandingPage1"])
                element2 = self.find_element("cssSelector", LogInPageMap["LoginLandingPage1"])
            except:
                element2 = self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["LivePlaynow"])
                element2 = self.find_element("cssSelector", LogInPageMap["LivePlaynow"])

            # click on the first play for real
            element2.click()

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
                    self.appendtofile(2, "Info Newgame pasge Successful Log in ")
                    print("Successful Log in")



            except:
                self.appendtofile(1, "Bug Failure Newgame User name is not displayed!!")
                raise Exception(" user name is not displayed")

    def logout(self):

        self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["logout"])
        element2 = self.find_element("cssSelector", CasinoPageMapXpath["logout"])
        element2.click()
        time.sleep(2)
        self.click(10,"cssSelector",HomePageMapXpath["topcasinoLocator"])
        time.sleep(2)
        self.newgames = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["newgameLocator"])
        self.newgames.click()
        time.sleep(2)

        self.newgames = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["newgameLocator"])
        self.newgames.click()
        time.sleep(2)

    def nothanks(self):
        try:
            element3 = self.find_element("cssSelector", HomePageMapXpath["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"

    def appendtofile(self, k, string):# k= 1 is observed missing bug, k = 2 only information of tested
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