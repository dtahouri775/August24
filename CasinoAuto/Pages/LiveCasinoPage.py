'''
Created on December 07, 2018

@author: Daryoush
'''
from CasinoAuto.Locators.UIMapLiveCasino import LiveCasinoPageMap
#from CasinoAuto.Locators.UIMapLiveCasino import LiveRoulettePageMap
from BasePage import IncorrectPageException
from BasePage import BasePage


class LiveCasinoPageM(BasePage):
    def __init__(self, driver):
        super( LiveCasinoPageM, self).__init__(driver)
        webElementsList = driver.find_elements_by_xpath('//img')
        global gamenum
        gamenum = len(webElementsList)
        print(gamenum)
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


