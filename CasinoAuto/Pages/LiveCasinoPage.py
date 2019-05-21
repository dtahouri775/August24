'''
Created on December 07, 2018

@author: Daryoush
'''
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
#from CasinoAuto.Locators.UIMapLiveCasino import LiveRoulettePageMap
from BasePage import IncorrectPageException
from BasePage import BasePage
import datetime

class LiveCasinoPageM(BasePage):
    def __init__(self, driver):
        super( LiveCasinoPageM, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        print(gamenum)
        self.appendtofile(2,"In Live Casino Page images="+str(gamenum))
        try:
            element = self.find_element("cssSelector", LiveCasinoPageMap["AcceptCookies"])
            element.click()
        except:
            print("Cookies dialog box is not there")

    def _verify_page(self):
        try:
            self.click(10, "cssSelector", LiveCasinoPageMap["livecasinoLocatortop"])
            self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveLobby"])
            self.wait_for_element_visibility(10, "cssSelector",LiveCasinoPageMap["LiveRoulette"])
            self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBlackjack"])
            #October 11 updated Home page
            self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBaccarat"])
            self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePoker"])
            self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveOthers"])


        except:
            raise IncorrectPageException

    def getgamenumber(self):
        return gamenum

    def livelobbymenu(self):

        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveLobby"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveLobby"])
        element1.click()

    def liveroulette(self):
        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveRoulette"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveRoulette"])
        element1.click()

    def liveblackjack(self):

        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBlackjack"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveBlackjack"])
        element1.click()

    def livebaccarat(self):

        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveBaccarat"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveBaccarat"])
        element1.click()

    def livepoker(self):

        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LivePoker"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LivePoker"])
        element1.click()

    def liveothergames(self):

        element1 = self.wait_for_element_visibility(10, "cssSelector", LiveCasinoPageMap["LiveOthers"])
        element1 = self.find_element("cssSelector", LiveCasinoPageMap["LiveOthers"])
        element1.click()


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