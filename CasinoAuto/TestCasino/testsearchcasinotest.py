'''
Created on Aug 20, 2018

@author: Daryoush
'''
#from selenium import webdriver
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
#from CasinoAuto.Pages.HomePage import HomePage
from CasinoAuto.Pages.CasinoPage import CasinoPage

class searchcasinotest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(searchcasinotest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL']+"/casino")
        self.driver.maximize_window()
        
    
    def test_SearchTrendigProductTest(self):
        search_page_obj = CasinoPage(self.driver)
        #enter an specific unique gagme name here for the testing of seeing only one results
        testitem1='fortunes of Arabia'
        search_page_obj.submit_request_search(testitem1)
        time.sleep(2)
        testitem2 = "fortuneOfArabia"
        search_page_obj.verifygamExisting(testitem2)#verify the result of fortune of Arabia as a test result

        time.sleep(3)

    def tearDown(self):
        super(searchcasinotest, self).tearDown()
        

if __name__ == "__main__":
    #unittest.main()
    nose.main()    