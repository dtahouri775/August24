'''
Created on Aug 14, 2018

@author: Daryoush
'''

from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath

from BasePage import IncorrectPageException

from BasePage import BasePage


class HomePageM(BasePage):
    def __init__(self, driver):
        super(HomePageM, self).__init__(driver)

    def _verify_page(self):
        try:

            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhncasinoLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["topcasinoLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["livecasinoLocatortop"])
            #October 11 updated Home page
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["lhnlivecasinoLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["promotionsLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["podcastLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["insightsLocator"])
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["appsLocator"])


        except:
            raise IncorrectPageException

    def lhn(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["lhncasinoLocator"]
                   )

    def top(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["topcasinoLocator"]
                   )

    def livecasino(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["livecasinoLocatortop"]
                   )

    def lhnlivecasino(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["lhnlivecasinoLocator"]
                   )

    def promotions(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["promotionsLocator"]
                   )
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["casinopromotionsLocator"]
                   )

    def podcast(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["podcastLocator"]
                   )
    def insights(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["insightsLocator"]
                   )
    def apps(self):
        self.click(10,
                   "cssSelector",
                   HomePageMapXpath["appsLocator"]
                   )