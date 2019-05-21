'''
Created on November 23, 2018

@author: Daryoush
'''
from CasinoAuto.Locators.UIMapCasinoPage import  CasinoPageMapXpath
from CasinoAuto.Locators.UIMAPPopularGamesPage import  PopularPageMap
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Constants                                import Casino_Constants
from MatchBookLoginPage import MatchBookLoginPage
from BasePage                import BasePage
import time
import datetime
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath


class PopularGamePage(BasePage):
    def __init__(self, driver):
        super(PopularGamePage, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)



#defining the casino page object here
    def  _verify_page(self):
        try:

            self.pggames = self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["popularLocator"])
            self.pggames.click()

        except:
            self.appendtofile(1, "Failure bug: Popular page: popular locator is not accessable ")
            raise Exception("popularLocator not accessable")


    def getgamenumber(self):
        return gamenum
    def verifysegration(self ):
        #seg="None"
        try:
            self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["popularslottitle"])
            element3 = self.find_element("cssSelector", PopularPageMap["popularslottitle"])
            time.sleep(1)
        except:
            self.appendtofile(1, "Failure bug Popular page: popularslot_title locator is not accessable ")
            raise Exception("popularslottitleis not accessable")

        try:
            self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["popularslottitle"])
            element3 = self.find_element("cssSelector", PopularPageMap["popularslottitle"])
            time.sleep(1)
        except:
            self.appendtofile(1, "Failure bug Popular page: popular slot title locator is not accessable! ")
            raise Exception("popularslottitleis not accessable")
        try:
            self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["popularlivetitle"])
            element3 = self.find_element("cssSelector", PopularPageMap["popularlivetitle"])
            time.sleep(1)
        except:
            self.appendtofile(1, "Failure bug Popular page: popularlive locator is not accessable!! ")
            raise Exception("popularlivetitle not accessable")
        try:
            self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["populartabletitle"])
            element3 = self.find_element("cssSelector", PopularPageMap["populartabletitle"])
            time.sleep(1)
        except:
            self.appendtofile(1, "Failure bug Popular page: popular tab locator is not accessable!!! ")
            raise Exception("populartabletitle not accessable")
        try:
            self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["popularvptitle"])
            element3 = self.find_element("cssSelector", PopularPageMap["popularvptitle"])
            time.sleep(1)
        except:
            self.appendtofile(1, "Failure bug Popular page: popularvp locator is not accessable ")
            raise Exception(" popularvptitle not accessable")

    def verifylandingpageinfo(self,a):#only testing for Red do not need to be here and needs to be removed

        element1 = self.wait_for_element_visibility(10, "cssSelector", PopularPageMap["popuolarlivegame1"])
        element1 = self.find_element("cssSelector",PopularPageMap["popuolarlivegame1"])
        # The game i is clicked and access to landing page
        element1.click()
        #time.sleep(1)

        # verify landing page game information
        #verify game name
        try:
            gamename = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgname"])
            gamename = self.find_element("cssSelector", CasinoPageMapXpath["LPgname"])
            text = gamename.text
            print(text)
        except:
            self.appendtofile(1, "Failure bug Popular page: Gamename locator is not accessable ")
            raise Exception("Game Name is not available Bug :200")
        print("Game name is: ",text)
        self.appendtofile(1, "Info Popular page: Game Name is ok ")
        #verify game provider
        try:
            gameprovider = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPprovider"])
            gameprovider = self.find_element("cssSelector", CasinoPageMapXpath["LPprovider"])

        except:
            self.appendtofile(1, "Failure bug Popular page: Game Provider locator is not accessable ")
            raise Exception("Game Provider is not available Bug :201")

        #verify game rule is there
        try:
            gamerule = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamerule"])
            gamerule = self.find_element("cssSelector", CasinoPageMapXpath["LPgamerule"])

        except:
            self.appendtofile(1, "Failure bug Popular page: Game rule  locator is not accessable ")
            raise Exception("Game Rule is not available Bug :201")

            # verify game description is there
        try:
            gamedes = self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
            gamedes = self.find_element("cssSelector", CasinoPageMapXpath["LPgamedescriptionredtiger"])
            text = gamedes.text
            print("Game description is:",text)
            self.appendtofile(1, "Info Popular page: Game Descrtiption is ok")
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
                    self.appendtofile(1, "Failure bug Popular page: Game description  locator is not accessable ")
                    raise Exception("Bug Game Descritpin is not available Bug :201")

        element1 = self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2 = self.find_element("cssSelector", HomePageMapXpath["lhncasinoLocator"])
        element2.click()
        time.sleep(1)
        element2.click()  # just to make sure
        self.click(10,"cssSelector",CasinoPageMapXpath["videopokerlocator"])

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