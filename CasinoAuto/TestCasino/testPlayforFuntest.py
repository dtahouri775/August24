'''
Created on November 20, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.SlotsPage import SlotsPage
from CasinoAuto.Pages.TableGamesPage import TableGamesPage
from CasinoAuto.Pages.CasinoPage import CasinoPage
from CasinoAuto.Pages.VideoPokerPage import VideoPokerPage
class playforfuntest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super( playforfuntest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def testplayforfunfromLandingpageSlotest(self):

            sg_page_obj = SlotsPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12
            mystr = "None"
            print("Number of game in this page equals: ",ng)
            time.sleep(3)
            casino_page_obj = CasinoPage(self.driver)
            for i in range(1,ng-6):  # footer images are deducted (- 6)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                mystr=sg_page_obj.click_playforfunfromlandingpageslot(i)
                print(mystr)
                temp = mystr[-4:]
                print(temp)
                if(temp=="demo"):
                    print("pass:",i)
                else:
                    print("The play for fun is not functioning correcly please check manually the link: ", mystr)
                casino_page_obj.slotgames()
                print("i= ", i)

    def testplayforfunfromLandingpageTableGames(self):

        sg_page_obj = TableGamesPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        mystr = "None"
        print("Number of game in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        for i in range(1, ng - 6):  # footer images are deducted (- 6)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            mystr = sg_page_obj.click_playforfunfromlandingpagetablegames(i)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            casino_page_obj.tablegames()
            print("i= ", i)

    def testplayforfunfromLandingpageVideopokers(self):

        sg_page_obj = VideoPokerPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        mystr = "None"
        print("Number of game in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        for i in range(1, ng - 5):  # footer images are deducted (- 5)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            mystr = sg_page_obj.click_playforfunfromlandingpagevpokergames(i)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            casino_page_obj.videopokergames()
            print("i= ", i)


    def tearDown(self):
        super( playforfuntest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()