'''
Created on Sept 04, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Pages.NewGamesPage import NewGamesPage
from CasinoAuto.Constants import Casino_Constants

class newgamestest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(newgamestest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def test_a_ztest(self):
        az_page_obj = NewGamesPage(self.driver)
        az_page_obj.verifyAZ()

    def test_z_atest(self):
        az_page_obj = NewGamesPage(self.driver)
        az_page_obj.verifyZA()

        time.sleep(2)
    def test_sort_a_ztest(self):
        az_page_obj = NewGamesPage(self.driver)
        az_page_obj.verifycorrectSortAZ()

    def test_sort_z_atest(self):
        za_page_obj = NewGamesPage(self.driver)
        za_page_obj.verifycorrectSortZA()

        # Verify user can access from each game landing page
    def testLoginFromLandingpageTest(self):

            ng_page_obj = NewGamesPage(self.driver)
            ng = ng_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=12#this number should be all the game in new game page plus five

            print("Number of images in this page equals: ",ng)
            for i in range(1,ng-6):  # footer images are deducted (- 6)
                ng_page_obj.click_loginfromlandingpage(i)
                ng_page_obj.logout()

    def tearDown(self):
        super(newgamestest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()