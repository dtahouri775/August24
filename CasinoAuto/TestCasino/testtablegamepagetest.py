'''
Created on Oct 12, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.TableGamesPage import TableGamesPage


class tablegpagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(tablegpagetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def test_a_ztest(self):
        az_page_obj = TableGamesPage(self.driver)
        print("Pass")

    def test_z_atest(self):
        az_page_obj = TableGamesPage(self.driver)
        az_page_obj.verifyZA()

        time.sleep(2)
    def test_sort_a_ztest(self):
        az_page_obj = TableGamesPage(self.driver)
        az_page_obj.verifycorrectSortAZ()

    def test_sort_z_atest(self):
        az_page_obj = TableGamesPage(self.driver)
        az_page_obj.verifycorrectSortZA()
    def testLoginfromLandingpageTest(self):

            sg_page_obj = TableGamesPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-6):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                gname=sg_page_obj.click_loginfromlandingpage(i)
                print(gname)
                sg_page_obj.logout()
                print("i= ", i)
    def testverifyGametypeTest(self):

            tg_page_obj = TableGamesPage(self.driver)
            ng = tg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                gname=tg_page_obj.veifygametype(i)
                print(gname)
                print("i= ", i)
    def testverifyMinMaxTopGameImageTest(self):#verify min-max and game name on top and bottom of game image

            tg_page_obj = TableGamesPage(self.driver)
            ng = tg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                gname=tg_page_obj.veifyminmax(i)
                print(gname)
                print("i= ", i)

    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):

        sg_page_obj = TableGamesPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 5):  # footer images are deducted (- 5)
        #for i in range(18, 19):  # checking only five of them, takes long checking for more than 110 games
            if(i!=9):
                gname = sg_page_obj.verifylandingpageinfo(i)
            print("i= ", i)

    def tearDown(self):
        super(tablegpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()