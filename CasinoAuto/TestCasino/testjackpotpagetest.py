'''
Created on Sept 06, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.JackPotsPage import  JackPotsPage


class jackpotgamestest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(jackpotgamestest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def test_a_ztest(self):
        az_page_obj = JackPotsPage(self.driver)
        az_page_obj.verifyAZ()

    def test_z_atest(self):
        az_page_obj =JackPotsPage(self.driver)
        az_page_obj.verifyZA()

        time.sleep(2)
    def test_sort_a_ztest(self):
        az_page_obj = JackPotsPage(self.driver)
        az_page_obj.verifycorrectSortAZ()

    def test_sort_z_atest(self):
        az_page_obj = JackPotsPage(self.driver)
        az_page_obj.verifycorrectSortZA()
        # Verify user can access from landing page

    def testLoginTest(self):

        jp_page_obj = JackPotsPage(self.driver)
        jp = jp_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            jp = 10

        print("Info Number of images in this page equals: ", jp)
        for i in range(1, jp - 5):  # footer images are deducted (- 6)
            jp_page_obj.click_loginfromlandingpage(i)
            jp_page_obj.logout(0)

    def testVerify_Jackpot_Amount_Displays_On_Landing_Page_Match_Image_value_Test(self):

        jp_page_obj = JackPotsPage(self.driver)
        jp = jp_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            jp = 10

        print("Info Number of images in this page equals: ", jp)
        for i in range(1, jp - 5):  # footer images are deducted (- 6)

            jp_page_obj.verifyjackpotamountlandingpage(i)
            jp_page_obj.logout(1)

    def tearDown(self):
        super(jackpotgamestest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()