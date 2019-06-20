'''
Created on Oct 12, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.SlotsPage import SlotsPage


class slotsgpagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(slotsgpagetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def test_a_ztest(self):
        az_page_obj = SlotsPage(self.driver)
        az_page_obj.verifyAZ()
        print("Pass")

    def test_z_atest(self):
        az_page_obj =SlotsPage(self.driver)
        az_page_obj.verifyZA()

        time.sleep(2)
    def test_sort_a_ztest(self):
        az_page_obj = SlotsPage(self.driver)
        az_page_obj.verifycorrectSortAZ()

    def test_sort_z_atest(self):
        az_page_obj = SlotsPage(self.driver)
        az_page_obj.verifycorrectSortZA()
    def testLoginfromLandingpageTest(self):

            sg_page_obj = SlotsPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(188,ng-6):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                print("Going to landing page= ", i)
                gname=sg_page_obj.click_loginfromlandingpage(i)
                print("Returning from landing page= ", i)
                print(gname)
                sg_page_obj.logout()
                print("i= ", i)

    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):

        sg_page_obj = SlotsPage(self.driver)
        ng = sg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 5):  # footer images are deducted (- 5)
            # for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
            gname = sg_page_obj.verifylandingpageinfo(i)
            print("i= ", i)
    def testverifyGametypeTest(self):

            sg_page_obj = SlotsPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)
            #for i in range(1, 10):  # checking only five of them, takes long checking for more than 110 games
                gname=sg_page_obj.veifygametype(i)
                print(gname)
                print("i= ", i)


    def tearDown(self):
        super(slotsgpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()