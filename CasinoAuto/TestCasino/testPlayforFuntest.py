'''
Created on November 20, 2018

@author: Daryoush
Modified on Feb 04 2019 to implement new logic in Play for Fun
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
            print("Number of images in this page equals: ",ng)
            time.sleep(3)
            casino_page_obj = CasinoPage(self.driver)
            casino_page_obj.click_logintop_button()#January 30 2019 only logged in player can play for fun!
            for i in range(1,ng-6):  # footer images are deducted (- 6)
                sg_page_obj.nothanks()
                mystr=sg_page_obj.click_playforfunfromlandingpageslot(i,1)#1 means already logged in
                time.sleep(2)
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
        print("Number of images in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.click_logintop_button()  # January 30 2019 only logged in player can play for fun!
        for i in range(1, ng - 6):  # footer images are deducted (- 6)
            sg_page_obj.nothanks()
            mystr = sg_page_obj.click_playforfunfromlandingpagetablegames(i,1)
            time.sleep(2)
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
        print("Number of images in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.click_logintop_button()  # January 30 2019 only logged in player can play for fun!
        for i in range(1, ng - 6):  # footer images are deducted (- 6)
            sg_page_obj.nothanks()
            mystr = sg_page_obj.click_playforfunfromlandingpagevpokergames(i, 1)
            time.sleep(2)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            casino_page_obj.tablegames()
            print("i= ", i)

    #may be implemented after test case is created,
    #player must be prompted for log in, otherwise fails the test
    def test_nonlogged_in_playerwillbepromptedforloginslotstest(self):
        sg_page_obj = SlotsPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        mystr = "None"
        print("Number of images in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        #casino_page_obj.click_logintop_button()  # January 30 2019 only logged in player can play for fun!
        for i in range(1, ng - 6):  # footer images are deducted (- 6)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            sg_page_obj.nothanks()
            mystr = sg_page_obj.click_playforfunfromlandingpageslot(i,0)#0 means has not been logged in user
            time.sleep(2)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            sg_page_obj.nothanks()
            sg_page_obj.logout()
            time.sleep(2)
            casino_page_obj.slotgames()

            print("i= ", i)

    def test_nonlogged_in_playerwillbepromptedforlogintablegametest(self):
        sg_page_obj = TableGamesPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        mystr = "None"
        print("Number of images in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        # casino_page_obj.click_logintop_button()  # January 30 2019 only logged in player can play for fun!
        for i in range(1, ng - 6):  # footer images are deducted (- 6)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            sg_page_obj.nothanks()
            mystr = sg_page_obj.click_playforfunfromlandingpagetablegames(i, 0)  # 0 means has not been logged in user
            time.sleep(2)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            sg_page_obj.nothanks()
            sg_page_obj.logout()
            time.sleep(2)
            casino_page_obj.slotgames()

            print("i= ", i)
    def test_nonlogged_in_playerwillbepromptedforloginvpokergametest(self):
        sg_page_obj = VideoPokerPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12
        mystr = "None"
        print("Number of images in this page equals: ", ng)
        time.sleep(3)
        casino_page_obj = CasinoPage(self.driver)
        # casino_page_obj.click_logintop_button()  # January 30 2019 only logged in player can play for fun!
        for i in range(1, ng - 5):  # footer images are deducted (- 6)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            sg_page_obj.nothanks()
            mystr = sg_page_obj.click_playforfunfromlandingpagevpokergames(i, 0)  # 0 means has not been logged in user
            time.sleep(2)
            print(mystr)
            temp = mystr[-4:]
            print(temp)
            if (temp == "demo"):
                print("pass:", i)
            else:
                print("The play for fun is not functioning correcly please check manually the link: ", mystr)
            sg_page_obj.logout()
            time.sleep(2)
            casino_page_obj.videopokergames()

            print("i= ", i)


    def tearDown(self):
        super( playforfuntest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()