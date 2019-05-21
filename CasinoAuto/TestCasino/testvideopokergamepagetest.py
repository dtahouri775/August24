'''
Created on Oct 12, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.VideoPokerPage import  VideoPokerPage


class videopokergamepagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(videopokergamepagetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def test_a_ztest(self):
        az_page_obj = VideoPokerPage(self.driver)
        print("Pass")

    def test_z_atest(self):
        az_page_obj = VideoPokerPage(self.driver)
        az_page_obj.verifyZA()

        time.sleep(2)
    def test_sort_a_ztest(self):
        az_page_obj = VideoPokerPage(self.driver)
        az_page_obj.verifycorrectSortAZ()

    def test_sort_z_atest(self):
        az_page_obj = VideoPokerPage(self.driver)
        az_page_obj.verifycorrectSortZA()
    def testLoginfromLandingpageTest(self):

            sg_page_obj = VideoPokerPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)

                gname=sg_page_obj.click_loginfromlandingpage(i)
                print(gname)
                sg_page_obj.logout()
                time.sleep(5);
                print("i= ", i)

    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):

        sg_page_obj = VideoPokerPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 5):  # footer images are deducted (- 5)
            gname = sg_page_obj.verifylandingpageinfo(i)
            print("i= ", i)

    def testverifyGametypeTest(self):

            vpg_page_obj = VideoPokerPage(self.driver)
            ng = vpg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                gname=vpg_page_obj.veifygametype(i)
                print(gname)
                print("i= ", i)

    def tearDown(self):
        super(videopokergamepagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()